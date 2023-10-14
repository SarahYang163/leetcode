import os
import threading
import sqlalchemy
from English.EnglishLearnAndReview.constants import sql_all_id_and_score, mysql_setting
from English.EnglishLearnAndReview.displays.displaySteps import get_word_probability, pronunciation, \
    choose_word, display

# 链接DB
engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}".format(**mysql_setting),
                                  max_overflow=5)
# 查出所有的记录
results = engine.connect().exec_driver_sql(sql_all_id_and_score)
# 将记录格式为字典
data = [dict(zip(results.keys(), result)) for result in results]
# 计算概率
probabilities = [get_word_probability(word["score"]) for word in data]
# 以上步骤不用再每次循环中多次调用
while 1:
    try:
        # 调用选择函数
        chosen_word = choose_word(engine, data, probabilities)
        # 发音和展示用线程方式同步进行
        t1 = threading.Thread(target=pronunciation(chosen_word))
        t1.start()

        t2 = threading.Thread(target=display(engine, chosen_word))
        t2.start()

        t1.join()
        t2.join()
        # Check if the file exists
        if os.path.exists("/Users/sarahyang/PycharmProjects/leetcode/English/temp.mp3"):
            # Delete the file
            os.remove("/Users/sarahyang/PycharmProjects/leetcode/English/temp.mp3")
            print("File deleted successfully.")
        print("\n")
    except Exception as e:
        print("while Error:", str(e))
