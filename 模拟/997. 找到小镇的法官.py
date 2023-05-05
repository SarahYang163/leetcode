# https://leetcode.cn/problems/find-the-town-judge/
from typing import List
import numpy


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 初始化入度出度,rem[0]入度，rem[1]出度
        remember = numpy.zeros((n, 2), dtype=int)
        for t in trust:
            remember[t[0]-1][1] += 1
            remember[t[1]-1][0] += 1
        for i in range(len(remember)):
            if remember[i][0] == n - 1 and remember[i][1] == 0:
                return i + 1
        return -1


if __name__ == '__main__':
    # res = Solution()
    # print(res.findJudge(1, []))
    # test = numpy.zeros((2, 3), dtype=numpy.int)
    # print(test)
    # x3 = numpy.zeros((3, 2), dtype=int)
    # test = [[0 for i in range(2)] for j in range(3)]
    # print(x3)
    # print(x3[1][1])
    # print(test[1][1])
    apple = [[0 for i in range(2)] for j in range(3)]
    print(apple)
