# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
from typing import List


# https://leetcode.cn/problems/combination-sum-ii/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()

        def process(candidates: List[int], target: int, index: int, res_tmp: List):
            if target == 0:
                self.res.append(res_tmp)
                return

            for i in range(index, len(candidates)):
                if i > 0 and i>index and candidates[i] == candidates[i - 1]:
                    continue
                if target - candidates[i] < 0:
                    break
                process(candidates, target - candidates[i], i + 1, res_tmp + [candidates[i]])

        process(candidates, target, 0, [])
        return self.res


if __name__ == '__main__':
    res = Solution()
    # print(res.combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 24))
    print(res.combinationSum2([1, 1, 1, 3, 3, 5], 8))
