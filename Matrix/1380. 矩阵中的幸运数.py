# https://leetcode.cn/problems/lucky-numbers-in-a-matrix/
import sys
from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # help_matrix = matrix
        arr1 = []
        arr2 = []
        res=[]
        for m in matrix:
            arr1.append(sorted(m)[0])
        for j in range(len(matrix[0])):
            max_ = -sys.maxsize - 1
            for i in range(len(matrix)):
                max_ = max(matrix[i][j], max_)
            arr2.append(max_)
        for a in arr1:
            if a in arr2:
                res.append(a)
        return res


if __name__ == '__main__':
    a = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    # print(a.sort(key=lambda x0, x1: x0 - x1))
    res = Solution()
    print(res.luckyNumbers(a))
