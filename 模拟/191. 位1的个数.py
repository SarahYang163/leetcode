# https://leetcode.cn/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        res = 0
        while n != 0:
            if n % 2 == 1:
                res += 1
            n = n >> 1
        return res
