# https://leetcode.cn/problems/number-of-closed-islands/
from typing import List


class Solution:
    # def closedIsland(self, grid: List[List[int]]) -> int:
    #     m = len(grid) - 1
    #     n = len(grid[0]) - 1
    #     answer = 0
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if grid[i][j] == 0:
    #                 answer += 1
    #                 self.dfs(grid, i, j, m, n)
    #     return answer
    #
    # def dfs(self, grid: List[List[int]], i, j, m, n):
    #     if i < 0 or j < 0 or i > m or j > n or grid[i][j] == 1:
    #         return
    #     grid[i][j] = 1
    #     self.dfs(grid, i + 1, j, m, n)
    #     self.dfs(grid, i - 1, j, m, n)
    #     self.dfs(grid, i, j + 1, m, n)
    #     self.dfs(grid, i, j - 1, m, n)
    def dfs(self, grid: List[List[int]], i, j, m, n):
        if i < 0 or j < 0 or i > m or j > n or grid[i][j] == 1:
            return
        grid[i][j] = 1
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i, j + 1, m, n)
        self.dfs(grid, i, j - 1, m, n)

    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        answer = 0
        for x in range(0, m + 1):
            self.dfs(grid, x, 0, m, n)
            self.dfs(grid, x, n, m, n)
        for y in range(0, n + 1):
            self.dfs(grid, 0, y, m, n)
            self.dfs(grid, m, y, m, n)
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if grid[i][j] == 0:
                    answer += 1
                    self.dfs(grid, i, j, m, n)
        return answer


if __name__ == '__main__':
    gird = [[1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]

    gird = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]

    gird = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    gird = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 2, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 2, 2, 1, 1, 1],
            [1, 1, 1, 2, 2, 2, 2, 1, 0, 1],
            [1, 2, 2, 2, 2, 2, 1, 1, 1, 1],
            [1, 1, 2, 1, 2, 1, 3, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 3, 3, 3, 1],
            [1, 1, 1, 1, 1, 1, 3, 3, 3, 1],
            [1, 1, 1, 4, 4, 1, 3, 1, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    res = Solution()
    print(res.closedIsland(
        gird))
