import sys
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(days[-1] + 1)]
        # 设定一个days指标，标记应该处理 days 数组中哪一个元素
        days_idx = 0
        for i in range(1, len(dp)):
            # 若当前天数不是待处理天数，则其花费费用和前一天相同
            if i != days[days_idx]:
                dp[i] = dp[i - 1]
            else:
                # 若 i 走到了待处理天数，则从三种方式中选一个最小的
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                days_idx += 1
        return dp[-1]  # 返回最后一天对应的费用即可


if __name__ == '__main__':
    res = Solution()
    print(res.mincostTickets([1, 4, 6, 7, 8, 20], [1, 100, 10000]))
    # arr = [1, 2, 3, 4, 5]
    # print(arr[-2])
