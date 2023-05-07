# https://leetcode.cn/problems/rank-transform-of-an-array/
# 给你一个整数数组arr ，请你将数组中的每个元素替换为它们排序后的序号。
#
# 序号代表了一个元素有多大。序号编号的规则如下：
#
# 序号从 1 开始编号。
# 一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
# 每个数字的序号都应该尽可能地小。
#
#
# 示例 1：
#
# 输入：arr = [40,10,20,30]
# 输出：[4,1,2,3]
# 解释：40 是最大的元素。 10 是最小的元素。 20 是第二小的数字。 30 是第三小的数字。
#
from typing import List


class Solution:
    def arrayRankTransform(self, nums: List[int]) -> List[int]:
        n = len(nums)
        helpMap = {}
        helpArr = sorted(nums)
        i = 1
        for helpA in helpArr:
            if helpA not in helpMap:
                helpMap[helpA] = i
                i += 1
        print(helpMap)
        for j in range(n):
            nums[j] = helpMap.get(nums[j])
        return nums