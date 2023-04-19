from typing import List


# https://leetcode.cn/problems/max-area-of-island/


def process(grid: List[List[int]], i: int, j: int, m: int, n: int, count: int) -> int:
    if i < 0 or i > n or j < 0 or j > m or grid[i][j] != 1:
        return 0
    grid[i][j] = 2
    return process(grid, i + 1, j, m, n, count) + process(grid, i - 1, j, m, n, count) + \
           process(grid, i, j + 1, m, n, count) + process(grid,
                                                          i,
                                                          j - 1,
                                                          m, n,
                                                          count) + 1


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    # 高
    n = len(grid) - 1
    # 长
    m = len(grid[0]) - 1
    # res = 0
    count = 0
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if grid[i][j] == 1:
                # res += 1
                count = max(process(grid, i, j, m, n, 0), count)
    return count


if __name__ == '__main__':
    print(maxAreaOfIsland([[1, 1, 0, 0, 0],
                           [0, 1, 0, 1, 1],
                           [0, 0, 0, 1, 1],
                           [0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 1]]))