# 给定一个字符串，打印他所有的子序列包括空串
from typing import List


def printallsub(s: str, i: int, res: str) -> str:
    if i == len(s):
        print(res)
        return
    printallsub(s, i + 1, res + s[i])
    printallsub(s, i + 1, res)


if __name__ == '__main__':
    printallsub("abc", 0, "")
    # s="banana"
    # print("apple"+s[0])

