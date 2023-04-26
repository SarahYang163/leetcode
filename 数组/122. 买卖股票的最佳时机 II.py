# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1  # r当前元素
        res, pre = 0, prices[0]  # res结果集,pre记录前一个元素
        while r < len(prices):
            if prices[r] > pre:
                res += prices[r] - pre
            pre = prices[r]
            r += 1
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.maxProfit([56,5,7,56,6,37,6,7,8,46,7,3,2,6,67]))
