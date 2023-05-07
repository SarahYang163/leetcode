# https://leetcode.cn/problems/single-number-iii/
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        freq = collections.Counter(nums)
        for f in freq.items():
            if f[1] == 1:
                res.append(f[0])
        return res
