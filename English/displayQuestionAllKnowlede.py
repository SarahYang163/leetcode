import os
import random
import math
import sys
import threading
import time
from bs4 import BeautifulSoup

import pyttsx4
import requests
import sqlalchemy
import translate
import pygame

soup_context = [["basic", "word-exp"], ["webPhrase", "mcols-layout"], ["blng_sents_part dict-module", "mcols-layout"]]
mysql_setting = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    # 数据库名称
    'db': 'test',
    'charset': 'utf8'
}


def displayTranslator(context, soup_translate_content):
    try:
        for c in context:
            elements = soup_translate_content.find(class_=c[0]).find_all(class_=c[1])
            for element in elements:
                print(element.text)
    except Exception as e:
        print("Error:", str(e))


def get_word_probability(score):
    # 计算单词的概率，使用指数分布函数
    # 假设 lambda = 0.1，调整 lambda 的值可以控制分数与概率之间的关系
    # 分数越高，概率越小
    _lambda = 0.1
    return math.exp(-_lambda * score)


# 链接DB
engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}".format(**mysql_setting),
                                  max_overflow=5)


def choose_word():
    # 查出所有的记录
    results = engine.connect().exec_driver_sql(
        "select English,Chinese,score,id,frequency,table_name  from AllEnglishKnowledge A where A.table_name != 'sentence' ")
    # "select English,Chinese,score,id,frequency from AllEnglishKnowledge A where A.table_name= 'sentence' ")
    # 将记录格式为字典
    data = [dict(zip(results.keys(), result)) for result in results]
    # 计算概率
    probabilities = [get_word_probability(word["score"]) for word in data]
    # 根据概率选择单词
    chosen_word = random.choices(data, probabilities)[0]
    # 展示以及交互
    # question = chosen_word["Chinese"]

    # 金山词霸的接口，不好用舍弃
    # response = \
    #     (requests.get("https://dict.iciba.com/dictionary/word/suggestion",
    #                   params={"word": chosen_word["English"]})).json()[
    #         "message"]
    # 改用有道的接口
    # html_translate_content = requests.get("https://dict.youdao.com/result", params={"word": chosen_word["English"], "lang": "en"}).text
    # 创建 BeautifulSoup 对象，指定解析器为 lxml
    # soup = BeautifulSoup(html_translate_content, 'lxml')
    # 使用 find_all 方法提取所有具有 class="content" 的元素
    # elements = soup.find(class_="word-exp")
    if chosen_word["table_name"] == "sentence":
        question = chosen_word["Chinese"]
    else:
        # Chinese meaning by translator api
        soup_translate_content = BeautifulSoup(
            requests.get("https://dict.youdao.com/result", params={"word": chosen_word["English"], "lang": "en"}).text,
            'lxml')
        question = soup_translate_content.find(class_="word-exp").text
    randomInt = random.randint(0, 1)
    # 现在所有的单词句子都可以翻译了，不用这一段代码了
    # if response:
    #     question = response[0]["paraphrase"]
    #     # print(question)
    # else:
    #     # python现成的翻译库，不好用舍弃
    #     # translator = translate.Translator(from_lang="English", to_lang="chinese")
    #     question = chosen_word["Chinese"]
    answer = chosen_word["English"]
    print(chosen_word["id"], question if randomInt == 1 else answer)
    key = input("按下任意键继续...:")
    if key == "s":
        engine.dispose()
        sys.exit()
    print("答案：", answer if randomInt == 1 else question)
    if chosen_word["table_name"] != "sentence":
        displayTranslator(soup_context, soup_translate_content)
    return chosen_word


def pronunciation():
    # time.sleep(2)
    # pronunciationEngine = pyttsx4.init()
    # pronunciationEngine.setProperty('rate', 250)
    # pronunciationEngine.say(chosen_word["English"])
    # pronunciationEngine.runAndWait()
    # response = (requests.get("https://dict.iciba.com/dictionary/word/suggestion",
    #                          params={"word": chosen_word["English"]})).content
    response = requests.get(
        'https://dict.youdao.com/dictvoice',
        params={"type": 1, "audio": chosen_word["English"]}).content  # 替换为实际的音频请求地址

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


def display():
    score = input("答案正确请输入1，答案错误请输入0:")
    sql1 = "update  AllEnglishKnowledge set score ={}-1 , frequency={}+1 where id ={}".format(chosen_word["score"],
                                                                                              chosen_word[
                                                                                                  "frequency"],
                                                                                              chosen_word["id"]
                                                                                              )
    sql0 = "update  AllEnglishKnowledge set score ={}+1 , frequency={}+1 where id ={}".format(chosen_word["score"],
                                                                                              chosen_word[
                                                                                                  "frequency"],
                                                                                              chosen_word["id"])
    try:
        with engine.begin() as conn:
            if score == "0":
                conn.execute(sqlalchemy.text(sql0))
            else:
                conn.execute(sqlalchemy.text(sql1))
    except Exception as e:
        print(e)
    engine.dispose()


while 1:
    try:
        chosen_word = choose_word()
        # pronunciation()
        # display()
        t1 = threading.Thread(target=pronunciation)
        t1.start()

        t2 = threading.Thread(target=display)
        t2.start()

        t1.join()
        t2.join()
        # Check if the file exists
        if os.path.exists("/Users/sarahyang/PycharmProjects/leetcode/English/temp.mp3"):
            # Delete the file
            os.remove("/Users/sarahyang/PycharmProjects/leetcode/English/temp.mp3")
            print("File deleted successfully.")
        print("\n")
        # del t1
        # del t2
    except Exception as e:
        print("Error:", str(e))
