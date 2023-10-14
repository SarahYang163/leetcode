import datetime
import time

import sqlalchemy

from English.EnglishLearnAndReview.constants import mysql_setting


class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            print("秒表已启动")

    def pause(self):
        if self.is_running:
            self.elapsed_time += time.time() - self.start_time
            self.is_running = False
            print("秒表已暂停")

    def resume(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            print("秒表已继续")

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False
        print("秒表已重置")

    def display_time(self):
        if self.is_running:
            current_elapsed = self.elapsed_time + time.time() - self.start_time
        else:
            current_elapsed = self.elapsed_time

        minutes = int(current_elapsed // 60)
        seconds = int(current_elapsed % 60)
        milliseconds = int((current_elapsed % 1) * 1000)

        print("{:02d}:{:02d}.{:03d}".format(minutes, seconds, milliseconds))
        return minutes


# 示例使用
stopwatch = Stopwatch()

while True:
    command = input("请输入命令（start/pause/resume/reset/display/quit）：")

    if command == "start":
        stopwatch.start()
    elif command == "pause":
        stopwatch.pause()
    elif command == "resume":
        stopwatch.resume()
    elif command == "reset":
        stopwatch.reset()
    elif command == "display":
        print("经过时间:", stopwatch.display_time())
    elif command == "quit":
        # 链接DB
        engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}".format(**mysql_setting),
                                          max_overflow=5)
        study_time = stopwatch.display_time()
        sql = "INSERT INTO StudyRecord (study_time) VALUES ({}) ".format(study_time)
        with engine.begin() as conn:
            conn.execute(sqlalchemy.text(sql))
        print("经过时间:", study_time)
        break
    else:
        print("无效的命令，请重试！")
    print(datetime.datetime.now())
