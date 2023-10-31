import math
import random
import re
import sys
import time

import pygame
import requests
import sqlalchemy
from bs4 import BeautifulSoup

from English.EnglishLearnAndReview.constants import sql_update_delete, sql_all_field, \
    soup_context, sql_update_score_and_frequency_minus, sql_update_score_and_frequency_add, sql_update_delete_unused, \
    sql_update_important, sql_update_unimportant, sql_YDSentence_insert, sql_update_score_and_frequency_add2


# 从context(html类型中)提取属性
def displayTranslator(engine, context, soup_translateContent):
    try:
        for c in context:
            elements = soup_translateContent.find(class_=c[0]).find_all(class_=c[1])
            for element in elements:
                print(element.text)
                if c[0] == 'blng_sents_part dict-module':
                    try:
                        split_result = split_sentence(element.text)
                        if re.search(r"['\"]", split_result[0]):
                            split_result[0] = split_result[0].replace("'", "\\'")
                            split_result[0] = split_result[0].replace('"', '\\"')
                        sql = sql_YDSentence_insert.format(split_result[0], split_result[1])
                        with engine.begin() as conn:
                            conn.execute(sqlalchemy.text(sql))
                    except Exception as e:
                        print("displayTranslator Error: ", str(e))
    except Exception as e:
        print("displayTranslator Error: ", str(e))


# 将有道自带句子收集插入表中，以下函数主要作用是处理分割句子
# 将句子排除开头的数字和后面词典信息，提取英文句子和中文含义
def split_sentence(sentence):
    pattern = r'([.?!。？！])'  # 匹配句子分割标点符号的正则表达式模式
    matches = re.split(pattern, sentence)  # 使用正则表达式进行分割
    result = []
    for i in range(0, len(matches), 2):
        if i + 1 < len(matches):
            # 去除开头的数字
            if re.match(r'^\d', matches[i]):
                result.append(matches[i][1:] + matches[i + 1])
            elif not matches[i].endswith("》"):
                result.append(matches[i])  # 句子部分
    return result


# 计算单词的概率，使用指数分布函数
def get_word_probability(score):
    # 假设 lambda = 0.1，调整 lambda 的值可以控制分数与概率之间的关系
    # 分数越高，概率越小
    _lambda = 0.1
    return math.exp(-_lambda * score)


# 发音模块，调用dict接口实现
def pronunciation(chosen_word):
    if chosen_word["table_name"] == 'sentence' or chosen_word["table_name"] == 'simple-sentence':
        return
    response = requests.get('https://dict.youdao.com/dictvoice',
                            params={"type": 0, "audio": chosen_word["English"]}).content  # 替换为实际的音频请求地址
    # 保存音频文件到临时文件
    audio_file = "temp.mp3"  # 临时文件名
    with open(audio_file, 'wb') as f:
        f.write(response)
    time.sleep(0.05)
    # 初始化 pygame
    pygame.init()
    # 加载音频文件
    pygame.mixer.music.load(audio_file)
    # 播放音频
    pygame.mixer.music.play()
    time.sleep(0.5)
    # 等待音频播放完毕
    while pygame.mixer.music.get_busy():
        continue
    # 清除临时文件
    pygame.mixer.music.stop()
    pygame.quit()


# 展示和交互模块
def display(engine, chosen_word):
    score = input("答案正确请输入1，答案错误请输入0:")
    sql1 = sql_update_score_and_frequency_minus.format(chosen_word["score"],
                                                       chosen_word["frequency"],
                                                       chosen_word["id"]
                                                       )
    sql0 = sql_update_score_and_frequency_add.format(chosen_word["score"],
                                                     chosen_word["frequency"],
                                                     chosen_word["id"])
    sql2 = sql_update_delete.format(chosen_word["score"],
                                    chosen_word["frequency"],
                                    chosen_word["id"])
    sql3 = sql_update_delete_unused.format(chosen_word["score"],
                                           chosen_word["frequency"],
                                           chosen_word["id"])
    sql4 = sql_update_important.format(chosen_word["score"],
                                       chosen_word["frequency"],
                                       chosen_word["id"])
    sql5 = sql_update_unimportant.format(chosen_word["score"],
                                         chosen_word["frequency"],
                                         chosen_word["id"])
    sql6 = sql_update_score_and_frequency_add2.format(chosen_word["score"],
                                                      chosen_word["frequency"],
                                                      chosen_word["id"]
                                                      )
    try:
        with engine.begin() as conn:
            if score == "1":
                conn.execute(sqlalchemy.text(sql0))
            elif score == "d":
                conn.execute(sqlalchemy.text(sql2))
            elif score == 'u':
                conn.execute(sqlalchemy.text(sql3))
            elif score == '-':
                conn.execute(sqlalchemy.text(sql4))
            elif score == '=':
                conn.execute(sqlalchemy.text(sql5))
            elif score == '0':
                pass
            elif score == '2':
                conn.execute(sqlalchemy.text(sql6))
            else:
                conn.execute(sqlalchemy.text(sql1))
    except Exception as e:
        print("update 更新数据库失败了：", e)
    finally:
        engine.dispose()


def choose_word(engine, data, probabilities):
    # 根据概率选择单词
    global soup_translate_content
    chosen_word_id = random.choices(data, probabilities)[0]["id"]
    chosen_words = engine.connect().exec_driver_sql(sql_all_field.format(chosen_word_id))
    chosen_word = [dict(zip(chosen_words.keys(), chosen_word)) for chosen_word in chosen_words][0]
    if chosen_word["table_name"] == "sentence" or chosen_word["table_name"] == "simple-sentence":
        question = chosen_word["Chinese"]
    else:
        try:
            # Chinese meaning by translator api
            soup_translate_content = BeautifulSoup(
                requests.get("https://dict.youdao.com/result",
                             params={"word": chosen_word["English"], "lang": "en"}).text, 'lxml')
            # 使用选择器定位到所有 col2 下除了 secondaryFont 属性的子元素 p
            target_ps = soup_translate_content.find(class_="trans-list").select('div.col2 > p:not(.secondaryFont)')
            # 提取每个标签的文本内容
            question = [p.get_text(strip=True) for p in target_ps]
        except Exception as e:
            question = chosen_word["Chinese"]
            print("choose_word Error:", str(e))
    randomInt = 1
    # random.randint(0, 1)
    answer = chosen_word["English"]
    print(chosen_word["id"], answer if randomInt == 1 else question)
    # if randomInt == 1:
    #     pronunciation(chosen_word)
    # if randomInt == 1 else answer)
    key = input("按下任意键继续...:")

    if key == "s":
        engine.dispose()
        sys.exit()
    print(soup_translate_content.find(class_="catalogue_tabs catalogue_author").find(class_="trans").text)
    print("答案：", question if randomInt == 1 else answer)
    if chosen_word["table_name"] != "sentence" and chosen_word["table_name"] != "simple-sentence":
        displayTranslator(engine, soup_context, soup_translate_content)
    return chosen_word
