# https://leetcode.cn/problems/most-profit-assigning-work/
from typing import List


class Solution:
    # 超时做法
    # def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    #     res = 0
    #     len_d = len(difficulty)
    #     worker.sort()
    #     seq = list(zip(profit, difficulty))
    #     seq.sort(reverse=-1)
    #     last_x = len_d-1
    #     for w in worker:
    #         x = 0
    #         while x <= last_x and x < len_d:
    #             if seq[x][1] <= w:  # 工人能做这个工作
    #                 res += seq[x][0]
    #                 last_x = x  # 记录上一个低级困难的走到了那个profit，原因低级别能完成的高级别一定能完成
    #                 break
    #             x += 1
    #     return res
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        seq = list(zip(difficulty, profit))
        seq.sort()
        ans = i = best = 0
        for w in sorted(worker):
            while i < len(seq) and w >= seq[i][0]:
                best = max(best, seq[i][1])
                i += 1
            ans += best
        return ans


if __name__ == '__main__':
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    res = Solution()
    print(res.maxProfitAssignment(difficulty, profit, worker))
