import math
import random
import sys
import time

import pygame
import requests
import sqlalchemy
from bs4 import BeautifulSoup

from English.EnglishLearnAndReview.constants import sql_update_delete, sql_all_field, \
    soup_context, sql_update_score_and_frequency_minus, sql_update_score_and_frequency_add


# 从context(html类型中)提取属性
def displayTranslator(context, soup_translateContent):
    try:
        for c in context:
            elements = soup_translateContent.find(class_=c[0]).find_all(class_=c[1])
            for element in elements:
                print(element.text)
    except Exception as e:
        print("displayTranslator Error: ", str(e))


# 计算单词的概率，使用指数分布函数
def get_word_probability(score):
    # 假设 lambda = 0.1，调整 lambda 的值可以控制分数与概率之间的关系
    # 分数越高，概率越小
    _lambda = 0.1
    return math.exp(-_lambda * score)


# 发音模块，调用dict接口实现
def pronunciation(chosen_word):
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
    try:
        with engine.begin() as conn:
            if score == "1":
                conn.execute(sqlalchemy.text(sql0))
            elif score == "d":
                conn.execute(sqlalchemy.text(sql2))
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
    if chosen_word["table_name"] == "sentence":
        question = chosen_word["Chinese"]
    else:
        # Chinese meaning by translator api
        soup_translate_content = BeautifulSoup(
            requests.get("https://dict.youdao.com/result", params={"word": chosen_word["English"], "lang": "en"}).text,
            'lxml')
        question = soup_translate_content.find(class_="word-exp").text
    # randomInt = random.randint(0, 1)
    answer = chosen_word["English"]
    print(chosen_word["id"], question)
    # if randomInt == 1 else answer)
    key = input("按下任意键继续...:")

    if key == "s":
        engine.dispose()
        sys.exit()
    print("答案：", answer)
    # if randomInt == 1 else question)
    if chosen_word["table_name"] != "sentence":
        displayTranslator(soup_context, soup_translate_content)
    return chosen_word
