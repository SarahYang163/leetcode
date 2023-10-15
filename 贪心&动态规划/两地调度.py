# https://leetcode.cn/problems/two-city-scheduling/
import heapq
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])

        total = 0
        n = len(costs) // 2
        # To optimize the company expenses,
        # send the first n persons to the city A
        # and the others to the city B
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total
        # total = 0
        # n = len(costs) // 2
        # array = []
        # for i in range(len(costs)):
        #     heapq.heappush(array, (costs[i][0] - costs[i][1], i))
        # for j in range(len(array)):
        #     if j < n:
        #         total += costs[heapq.heappop(array)[1]][0]
        #     else:
        #         total += costs[heapq.heappop(array)[1]][1]
        # return total


if __name__ == '__main__':
    res = Solution()
    print(res.twoCitySchedCost(
        [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]))
    # array = [4, 5, 2, 4, 7, 32, 1]
    # x = sorted(array)
    # print(array)
    L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
    # 2、利用参数 cmp 排序
    # a = sorted(L, cmp=lambda x, y: cmp(x[1], y[1]))
    # 结果：
    # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    # 3、利用参数 key 排序
    b = sorted(L, key=lambda x: x[1], reverse=0)
    # 结果：
    # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    # 4、按年龄升序
    students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    c = sorted(students, key=lambda s: s[2])
    # 结果：
    # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    # 5、按年龄降序
    d = sorted(students, key=lambda s: s[2], reverse=True)
    # 结果：
    # [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    total = 0
    n = len(costs) / 2
    costs.sort(key=lambda x: x[0] - x[1])
    for i in range(n):
        total += costs[i][0] + costs[i + n][1]
    print(total)
