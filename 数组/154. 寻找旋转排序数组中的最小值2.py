# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/
import sys
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        mi, ma = -sys.maxsize - 1, sys.maxsize
        n = len(nums)
        l, r = 0, n - 1
        while r >= 0 and l < n:
            if nums[l] >= mi:
                mi = nums[l]
                l += 1
            else:
                return nums[l]
            if nums[r] <= ma:
                ma = nums[r]
                r -= 1
            else:
                return ma
        return nums[0] if nums[0] < nums[n - 1] else nums[n - 1]


if __name__ == '__main__':
    res = Solution()
    print(res.findMin([2, 1]))
