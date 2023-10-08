import random
import math
import sys

import pyttsx4
import requests
import sqlalchemy
import translate

mysql_setting = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    # 数据库名称
    'db': 'test',
    'charset': 'utf8'
}

# 链接DB
engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}".format(**mysql_setting),
                                  max_overflow=5)


def get_word_probability(score):
    # 计算单词的概率，使用指数分布函数
    # 假设 lambda = 0.1，调整 lambda 的值可以控制分数与概率之间的关系
    # 分数越高，概率越小
    _lambda = 0.1
    return math.exp(-_lambda * score)


def choose_word():
    # 查出所有的记录
    results = engine.connect().exec_driver_sql("select English,Chinese,score,id from ieltsVocabulary  ")
    # 将记录格式为字典
    data = [dict(zip(results.keys(), result)) for result in results]
    # 计算概率
    probabilities = [get_word_probability(word["score"]) for word in data]
    # 根据概率选择单词
    chosen_word = random.choices(data, probabilities)[0]
    # 展示以及交互
    # question = chosen_word["Chinese"]
    response = \
        (requests.get("https://dict.iciba.com/dictionary/word/suggestion",
                      params={"word": chosen_word["English"]})).json()[
            "message"]
    randomInt = random.randint(0, 1)
    if response:
        question = response[0]["paraphrase"]
        # print(question)
    else:
        # translator = translate.Translator(from_lang="English", to_lang="chinese")
        question = chosen_word["Chinese"]
    answer = chosen_word["English"]
    print(chosen_word["id"], question if randomInt == 1 else answer)
    key = input("按下任意键继续...:")
    if key == "s":
        engine.dispose()
        sys.exit()
    print("答案：", answer if randomInt == 1 else question)
    return chosen_word


def pronunciation():
    pronunciationEngine = pyttsx4.init()
    pronunciationEngine.setProperty('rate', 250)
    pronunciationEngine.say(chosen_word["English"])
    pronunciationEngine.runAndWait()


def display():
    score = input("答案正确请输入1，答案错误请输入0:")
    sql1 = "update  ieltsVocabulary set score ={}-1 where id ={}".format(chosen_word["score"], chosen_word["id"])
    sql0 = "update  ieltsVocabulary set score ={}+1 where id ={}".format(chosen_word["score"], chosen_word["id"])
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
    chosen_word = choose_word()
    pronunciation()
    display()
    # t1 = threading.Thread(target=pronunciation)
    # t1.start()
    #
    # t2 = threading.Thread(target=display)
    # t2.start()
    #
    # t1.join()
    # t2.join()
