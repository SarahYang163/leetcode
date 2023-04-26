# https://leetcode.cn/problems/contains-duplicate/
# 给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
# 输入：nums = [1,2,3,1]
# 输出：true
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        last_num = nums[0]
        for i in range(1, len(nums), ):
            if last_num == nums[i]:
                return True
            last_num = nums[i]

        return False

