from typing import List


# https://leetcode.cn/problems/next-greater-element-i/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        helpStack = []
        next_res2 = {}
        result = []
        for i in range(len(nums2)):
            while len(helpStack) != 0 and helpStack[-1][1] < nums2[i]:
                next_res2[helpStack[-1][1]] = nums2[i]
                helpStack.pop()
            helpStack.append([i, nums2[i]])
        for num in nums1:
            result.append(next_res2.get(num, -1))
        return result
