# https://leetcode.cn/problems/next-greater-element-ii/
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        helpStack = []
        duble_nums = nums + nums
        for i in range(len(duble_nums)):
            while len(helpStack) != 0 and helpStack[-1][1] < duble_nums[i]:
                # 记录下一个更大
                if helpStack[-1][0] < len(nums):
                    res[helpStack[-1][0]] = duble_nums[i]
                # 出栈
                helpStack.pop()
            helpStack.append([i, duble_nums[i]])
        return res
