# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
from typing import List


# https://leetcode.cn/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []

        def process(candidates: List[int], target: int, index: int, res_tmp: List):
            if target == 0:
                res_tmp.sort()
                if res_tmp not in self.res:
                    self.res.append(res_tmp)
                return
            for i in range(index, len(candidates)):
                if target - candidates[i] >= 0:
                    process(candidates, target - candidates[i], i, res_tmp + [candidates[i]])

        process(candidates, target, 0, [])

        return self.res

    def combinationSum4(self, candidates: List[int], target: int) -> int:

        self.res = 0
        candidates.sort()
        def process(candidates: List[int], target: int, res_tmp: List):
            if target == 0:
                self.res += 1
                return
            for i in range(0, len(candidates)):
                if target - candidates[i] < 0:
                    break
                process(candidates, target - candidates[i], res_tmp + [candidates[i]])

        process(candidates, target, [])

        return self.res


if __name__ == '__main__':
    res = Solution()
    print(res.combinationSum4([4, 2, 1], 30))
