# 方法1：共享变量--不推荐，会出现 线程安全问题
# 方法二：通过消息队列
from queue import Queue
