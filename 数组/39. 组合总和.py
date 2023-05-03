# https://leetcode.cn/problems/combination-sum/
from typing import List


# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
#

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort(reverse=True)
        for candidate in candidates:
            k = 0
            while target - candidate * k >= 0:
                if target - candidate * k in candidates:
                    tmp = []
                    for i in range(k):
                        tmp.append(candidate)
                    tmp.append(target - candidate * k)
                    tmp.sort()
                    if tmp not in res:
                        res.append(tmp)
                k += 1
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.combinationSum([2, 3, 5], 8))
