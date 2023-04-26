# https://leetcode.cn/problems/maximum-subarray/
import sys
from typing import List


class Solution:
    # 超时辣，因为时间复杂度O(n*n)
    # def maxSubArray(self, nums: List[int]) -> int:
    #     result = -sys.maxsize - 1
    #     l = 0
    #     while l < len(nums):
    #         r = l
    #         sunNum = 0
    #         while r < len(nums):
    #             sunNum += nums[r]
    #             result = max(result, sunNum)
    #             if sunNum <= 0:
    #                 break
    #             r += 1
    #         l += 1
    #     return result
    # 动态规划
    # f(i)=max{f(i−1)+nums[i],nums[i]}
    def maxSubArray(self, nums: List[int]) -> int:
        result = -sys.maxsize - 1
        l, pre = 0, -sys.maxsize - 1
        while l < len(nums):
            pre = max(pre + nums[l], nums[l])
            result = max(result, pre)
            l+=1
        return result


if __name__ == '__main__':
    res = Solution()
    print(res.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
