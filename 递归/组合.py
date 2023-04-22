from typing import List


# https://leetcode.cn/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(n: int, tmp: List, k: int):
            if len(tmp) == k:
                res.append(tmp)
                return
            if n == 0:
                return
            backtrack(n - 1, tmp + [n], k)
            backtrack(n - 1, tmp, k)

        backtrack(n, [], k)
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.combine(4, 3))
