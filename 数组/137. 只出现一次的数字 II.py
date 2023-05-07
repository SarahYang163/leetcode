# https://leetcode.cn/problems/single-number-ii/
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans


if __name__ == '__main__':
    # res = Solution()
    # print(res.singleNumber([0, 1, 0, 1, 0, 1, 99]))
    freq = collections.Counter([0, 1, 0, 1, 0, 1, 99])
    for f in freq.items():
        if f[1] == 1:
            print(f[0])
