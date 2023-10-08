import sys
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def quickSort(self, arr: list, start: int, end: int):
        # [3, 8, 2, 1, 4]
        if len(arr) == 0 or start >= end:
            return
        temp = arr[start]
        left = start
        right = end
        while left < right:
            while right > left and arr[right] >= temp:
                right -= 1
            arr[left] = arr[right]
            while left < right and arr[left] <= temp:
                left += 1
            arr[right] = arr[left]
        arr[right] = temp
        print(arr)
        self.quickSort(arr, start, right - 1)
        self.quickSort(arr, right + 1, end)

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize for _ in range(amount + 1)]
        dp[0] = 0
        print(dp)
        for coin in coins:
            for i in range(coin, amount + 1, 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        print(dp)
        return dp[amount]

    def divide(self, dividend: int, divisor: int) -> int:
        flag = False
        if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0):
            flag = True
        res = 0
        sum_divisor = 0
        while sum_divisor < dividend:
            res += 1
            sum_divisor += divisor
        return res - 1 if flag is True else -(res - 1)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            set_ = set()
            set_.add(nums[i])
            for j in range(i + 1, len(nums)):
                set_.add(nums[j])
                if -(nums[i] + nums[j]) not in set_:
                    set_.add((nums[i] + nums[j]))
                else:
                    print(nums[i], nums[j], -(nums[i] + nums[j]))
        return [[]]


if __name__ == '__main__':
    res = Solution()
    array = {2, 3, 5}
    array1 = {3, 8, 2, 1, 4}
    z = array.isdisjoint(array1)
    print(z)
    # print(array1 - array)
    # res.quickSort(array, 0, len(array) - 1)
    # print(array)
    coins = [1, 2, 5]
    amount = 11
    # print(res.coinChange(coins, amount))
    # print(res.divide(3, 7))
    res.threeSum([2, -1, 1, 1, 2])


    def outer_function(x):
        def inner_function(y):
            return x + y

        return inner_function


    closure = outer_function(10)
    result = closure(5)
    print(result)  # 输出 15