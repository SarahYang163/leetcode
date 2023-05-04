from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.res = []

        def process(arr: List, index: int, k: int, target: int, res_tmp: List):
            if target == 0 and k == 0:
                self.res.append(res_tmp)
                return
            for i in range(index, len(arr)):
                if target < 0:
                    break
                process(arr, i + 1, k - 1, target - arr[i], res_tmp + [arr[i]])

        process(arr, 0, k, n, [])
        return self.res
