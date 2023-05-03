from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set1 = set()
        set2 = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    set1.add(i)
                    set2.add(j)
        for i in range(len(matrix)):
            if i in set1:
                matrix[i] = [0] * len(matrix[0])
            else:
                for j in set2:
                    matrix[i][j] = 0


if __name__ == '__main__':
    res = Solution()
    print(res.setZeroes([[0, 1, 2, 0], [0, 3, 5, 2], [1, 3, 1, 5]]))
