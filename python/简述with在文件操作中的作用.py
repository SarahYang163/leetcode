# with open(r"", "r") as f:
#     script = f.read()
# 避免因读取文件时异常发生而没有关闭的问题了
# 就是以下的代码
f = open("abc.txt", "r")
data = f.read()
f.close()
