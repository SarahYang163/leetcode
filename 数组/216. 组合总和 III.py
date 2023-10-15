from typing import List


class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # self.res = []
        #
        # def process(arr: List, index: int, k: int, target: int, res_tmp: List):
        #     if target == 0 and k == 0:
        #         self.res.append(res_tmp)
        #         return
        #     for i in range(index, len(arr)):
        #         if target < 0:
        #             break
        #         process(arr, i + 1, k - 1, target - arr[i], res_tmp + [arr[i]])
        #
        # process(arr, 0, k, n, [])
        # return self.res

        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for num in range(1, 10, 1):
            for i in range(target, num - 1, -1):
                for a in dp[i - num]:
                    dp[i].append(a + [num])
        res = []
        for r in dp[target]:
            if len(r) == k:
                res.append(r)
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.combinationSum3(9, 45))
