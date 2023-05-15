# https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/
# 输入：events = [[1,2],[2,3],[3,4]]
# 输出：3
# 解释：你可以参加所有的三个会议。
# 安排会议的一种方案如上图。
# 第 1 天参加第一个会议。
# 第 2 天参加第二个会议。
# 第 3 天参加第三个会议。
import math
import bisect
from typing import List
import heapq

from whoosh.sorting import OrderedList


# https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/solution/python3-tan-xin-by-yim-6-dh1y/
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        ans = 0
        end = list()
        events = sorted(events, reverse=True)
        for i in range(1, 100010, 1):
            while events and events[-1][0] == i:
                heapq.heappush(end, events.pop()[1])
            while end and end[0] < i:
                heapq.heappop(end)
            if end:
                heapq.heappop(end)
                ans += 1
        return ans


if __name__ == '__main__':
    # res = Solution()
    # print(res.maxEvents([[1, 2], [2, 2], [3, 3], [3, 4], [3, 4]]
    #                     ))
    a = [5, 3, 5, 4, 322, 3]
    a.sort()
    print(a)
    af = bisect.bisect_right(a, 7)
    print(af)
    L = [1, 3, 3, 4, 6, 8, 12, 15]
    x_sect_point = bisect.bisect_left(L, 10)  # 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置
    print(x_sect_point)  # 1
    x_sect_point = bisect.bisect_left(L, 10)  # 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置
    print(x_sect_point)  # 4

    x_sect_point = bisect.bisect_right(L, 10)  # 在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置
    print(x_sect_point)  # 3
    x_sect_point = bisect.bisect_right(L, 5)  # 在L中查找x，x存在时返回x右侧的位置，x不存在返回应该插入的位置
    print(x_sect_point)  # 4

    bisect.insort_left(L, 2)  # 将x插入到列表L中，x存在时插入在左侧
    print(L)  # [1, 2, 3, 3, 4, 6, 8, 12, 15]

    bisect.insort_right(L, 4)  # 将x插入到列表L中，x存在时插入在右侧
    print(L)  # [1, 2, 3, 3, 4, 4, 6, 8, 12, 15]