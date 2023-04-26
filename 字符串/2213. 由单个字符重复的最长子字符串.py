# https://leetcode.cn/problems/longest-substring-of-one-repeating-character/
from typing import List


#
# 输入：s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
# 输出：[3,3,4]
# 解释：
# - 第 1 次查询更新后 s = "bbbacc" 。由单个字符重复组成的最长子字符串是 "bbb" ，长度为 3 。
# - 第 2 次查询更新后 s = "bbbccc" 。由单个字符重复组成的最长子字符串是 "bbb" 或 "ccc"，长度为 3 。
# - 第 3 次查询更新后 s = "bbbbcc" 。由单个字符重复组成的最长子字符串是 "bbbb" ，长度为 4 。
# 因此，返回 [3,3,4] 。
# 此算法超时
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        res = []
        for i in range(len(queryCharacters)):
            s = s[:queryIndices[i]] + queryCharacters[i] + s[queryIndices[i] + 1:]
            print(s)
            length = 1
            last_s = s[0]
            max_length = 1
            for j in range(1, len(s)):
                if s[j] == last_s:
                    length += 1
                else:
                    last_s = s[j]
                    length = 1
                max_length = max(max_length, length)
            res.append(max_length)
        return res


if __name__ == '__main__':
    res = Solution()
    # print(res.longestRepeating("abazzz", "zz", [2, 1]))
    # a=[1,2,3]
    # a.remove(4)