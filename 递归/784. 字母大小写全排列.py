# https://leetcode.cn/problems/letter-case-permutation/
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def process(s: str, i, tmp: str):
            if i == len(s):
                res.append(tmp)
                return
            if s[i].isdigit():
                process(s, i + 1, tmp + s[i])
            else:
                process(s, i + 1, tmp + s[i].upper())
                process(s, i + 1, tmp + s[i].lower())

        process(s, 0, "")
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.letterCasePermutation("a1b2"))
