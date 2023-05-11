# https://leetcode.cn/problems/sum-swap-lcci/
from typing import List, Tuple


class Solution:
    def findSwapValues(self, array1: Tuple[int], array2: List[int]) -> List[int]:
        sum1, sum2 = 0, 0
        sum1 = sum(array1)
        sum2 = sum(array2)
        if abs(sum1 - sum2) % 2 == 1:
            return []
        num = (sum1 - sum2) // 2
        set_ = set(array2)
        for arr1 in array1:
            if arr1 - num in set_:
                return [arr1, arr1 - num]
        return []
