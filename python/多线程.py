import threading
# io操作多线程和多进程区别不大

import time


class getDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(f"get detail html started", time.time())
        time.sleep(5)
        print(f"get detail html ended", time.time())


class getDetailUrl(threading.Thread):
    def __init__(self, name=None):
        # self.name = name
        super().__init__(name=name)

    def run(self):
        print(self.name)
        print(f"get url starting", time.time())
        time.sleep(4)
        print(f"get url ended", time.time())


# def get_detail_html():
#     print(f"get detail html started", time.time())
#     time.sleep(5)
#     print(f"get detail html ended", time.time())
#
#
# def get_detail_url():
#     print(f"get url starting", time.time())
#     time.sleep(4)
#     print(f"get url ended", time.time())


# # 方法1引用threading
# # damon is true meaning thread is protected thread
# thread1 = threading.Thread(target=get_detail_html, daemon=True)
# thread2 = threading.Thread(target=get_detail_url)
# start_time = time.time()
# thread1.start()
# thread2.start()
# # 下面的两行是说等thread执行完之后才执行主线程的代码
# # thread2.join()
# # thread1.join()
# print(start_time)
# print("main end")
# print(time.time())

# 方法二继承threading
demo = getDetailHtml("hhh")
demo.run()
demo2 = getDetailUrl("url")
demo2.run()
