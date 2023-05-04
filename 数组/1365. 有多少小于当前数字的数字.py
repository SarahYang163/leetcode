# https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        helpMap = {}
        helpArr = sorted(nums)
        for i in range(n):
            if helpArr[i] not in helpMap:
                helpMap[helpArr[i]] = i
        for j in range(n):
            nums[j] = helpMap.get(nums[j])

        return nums
