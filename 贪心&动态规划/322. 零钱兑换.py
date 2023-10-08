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

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < n:
                nums[i + 1] = nums[i]
                nums[i] = n
                nums = nums[:i + 1:] + sorted(nums[i + 1::])
                print("1")
                print(nums)
                return
            else:
                n = nums[i]
        nums = nums[::-1]
        print("nums")
        print(nums)
        return

    def jump(self, nums: List[int]) -> int:
        dp = [sys.maxsize for _ in range(len(nums))]
        dp[0] = 0
        for i in range(0, len(nums) - 1, 1):
            for j in range(i + 1, i + nums[i] + 1):
                if j < len(nums):
                    dp[j] = min(dp[i] + 1, dp[j])
        return dp[len(nums) - 1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[sys.maxsize for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i != 0 or j != 0:
                    dp[i][j] = min(dp[i - 1][j] if i > 0 else sys.maxsize, dp[i][j - 1] if j > 0 else sys.maxsize) + \
                               grid[i][j]
        return dp[len(grid) - 1][len(grid[0]) - 1]


if __name__ == '__main__':
    # nums = [1, 2, 2, 22, 2]
    # for i in range(len(nums) - 1, 0, -1):
    #     print(i)
    res = Solution()
    print(res.minPathSum([[1, 2, 3], [4, 5, 6]]))
