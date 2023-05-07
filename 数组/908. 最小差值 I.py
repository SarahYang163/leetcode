from typing import List

# https://leetcode.cn/problems/smallest-range-i/
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums)<=1:
            return 0
        nums.sort()
        print(nums)
        minN=nums[0]
        maxN=nums[-1]
        return maxN-minN-2*k if maxN-minN-2*k >=0 else 0