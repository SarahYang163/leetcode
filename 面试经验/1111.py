# encoding: utf-8
# a = input("please input a number:")
from typing import List


# print("hello world")
# nums = [-1, 0, 3, 5, 9, 1]
# target = 9


# def test(nums: list, target: int) -> int:
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         mid = left + right >> 1
#
#         if nums[mid] > target:
#             right = mid - 1
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             return mid
#     return -1


class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        i = 0
        while i < len(nums):
            if k - nums[i] in nums[i + 1:]:
                temp = nums[i]
                nums.remove(temp)
                nums.remove(k - temp)
                res += 1
            else:
                i += 1
        return res

    def removeStars(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i] == "*":
                s = s[:i - 1] + s[i + 1:]
                i -= 1
            else:
                i += 1
        return s

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[M][N]


# a=[2,3,1,5,3]
# b=[6,2,4,6,7]
    def test1(self,arr1: list, arr2: list) -> list:
        # 解法一：
        arr = sorted(arr1 + arr2)
        return arr


    def test2(self,arr1: list, arr2: list) -> list:
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)

        return quicksort(arr1 + arr2)


if __name__ == '__main__':
    res = Solution()
    a = [2, 3, 1, 5, 3]
    b = [6, 2, 4, 6, 7]
    print(res.test2(a, b))
