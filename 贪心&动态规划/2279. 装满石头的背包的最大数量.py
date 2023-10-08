# https://leetcode.cn/problems/maximum-bags-with-full-capacity-of-rocks/
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        count = 0
        combs = list(zip(capacity, rocks))
        combs.sort(key=lambda combs: combs[0] - combs[1])
        for comb in combs:
            tmp = comb[0] - comb[1]
            if additionalRocks >= tmp:
                count += 1
                additionalRocks -= tmp
            else:
                break
        return count



if __name__ == '__main__':
    res = Solution()
    print(res.maximumBags([10, 2, 2], [2, 2, 0], 100))
