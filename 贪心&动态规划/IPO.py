# https://leetcode.cn/problems/ipo/
from heapq import heapify, heappush, heappop

# class Solution:
#
#     def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
#         H1, H2 = List(zip[Capital, Profits]), []
#         heapq.heapify(H1)
#         for i in range(k):
#             while H1 and H1.pop()[0][Capital] <= W:
#                 heappush(H2, -H1.pop()[0][Profits])
#             if not H2:
#                 break
#             W -= heappop(H2)
#         return W

from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        H1, H2 = list(zip(Capital, Profits)), []
        heapify(H1)
        for i in range(k):
            while H1 and H1[0][0] <= W:
                heappush(H2, -heappop(H1)[1])
            if not H2:
                break
            W -= heappop(H2)
        return W


if __name__ == '__main__':
    ans = Solution()
    print(ans.findMaximizedCapital(2, 0, [3, 2, 1], [1, 1, 0]))
    # print("apple")
    # ll = [1, 4, 2, 3, 5]
    # print(ll, '原始数组')
    # heapify(ll)
    # print(ll, '小根堆')
    # 此时若想得到大顶堆
    # newl = [(-i, ll[i]) for i in range(len(ll))]
    # print(newl, '插入负数后的小根堆')
    # heapify(newl)  # 以插入的负数做小根堆，越大的数字插入的负数就越小，所以这样就相当于做了大根堆
    # # 此时已经按照第一个值变成了小顶堆，即变成了逆序
    # max_heap = list()
    # while newl:
    #     _, s = heappop(newl)  # 删除并返回 newl中的最小元素
    #     max_heap.append(s)
    # print(max_heap, '输出的大根堆')
