from typing import List


# https://leetcode.cn/problems/max-area-of-island/


def process(grid: List[List[int]], i: int, j: int, m: int, n: int):
    if i < 0 or i > n or j < 0 or j > m or grid[i][j] != 1:
        return
    grid[i][j] = 2
    process(grid, i + 1, j, m, n)
    process(grid, i - 1, j, m, n)
    process(grid, i, j + 1, m, n)
    process(grid, i, j - 1, m, n)


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    # 高
    n = len(grid) - 1
    # 长
    m = len(grid[0]) - 1
    res = 0
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if grid[i][j] == 1:
                res += 1
                process(grid, i, j, m, n)
    return res


if __name__ == '__main__':
    print(maxAreaOfIsland([[1, 1, 0, 0, 0],
                           [0, 1, 0, 1, 1],
                           [0, 0, 0, 1, 1],
                           [0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 1]]))