# https://leetcode.cn/problems/coin-change/
import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize for i in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1, 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != sys.maxsize else -1
