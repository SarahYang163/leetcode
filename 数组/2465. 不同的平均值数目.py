# https://leetcode.cn/problems/number-of-distinct-averages/
from typing import List

import setuptools.command.alias


class Solution:
    def distinctAverages(self, nums: List[int]) -> set:
        setRes = set()
        while len(nums) > 1:
            nums.sort()
            maxNum = nums[-1]
            minNum = nums[0]
            nums.remove(maxNum)
            nums.remove(minNum)
            zhong = (minNum + maxNum) / 2
            setRes.add(zhong)
        if len(nums) == 1:
            setRes.add(nums[0])
            return setRes
        if len(nums) == 0:
            return setRes


if __name__ == '__main__':
    res = Solution()
    print(res.distinctAverages([4, 1, 4, 0, 3, 5]))
