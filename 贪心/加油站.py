# https://leetcode.cn/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = 0
        sum_cost = 0
        for g in gas:
            sum_gas += g
        for c in cost:
            sum_cost += c
        if sum_gas < sum_cost:
            return -1
        start = 0
        Y_count = 0
        for i in range(len(gas)):
            Y_count += gas[i] - cost[i]
            if Y_count < 0:
                Y_count = 0
                start = i + 1
        return start


if __name__ == '__main__':
    res = Solution()
    print(res.canCompleteCircuit([4,3,1,2,7,4], [1,2,7,3,2,5]))
