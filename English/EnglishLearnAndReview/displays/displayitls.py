# 链接DB
import sys

import sqlalchemy

from English.EnglishLearnAndReview.constants import sql_itls, mysql_setting

engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}".format(**mysql_setting),
                                  max_overflow=5)
# 查出所有的记录
results = engine.connect().exec_driver_sql(sql_itls)
data = [dict(zip(results.keys(), result)) for result in results]

# 以上步骤不用在每次循环中多次调用
count = 0
while 1:
    for d in data:
        count += 1
        print(count, d["question"])
        key = input("按下任意键继续...:")
        if key == "s":
            engine.dispose()
            sys.exit()
        print("答案：", d['answers'], '\n')
