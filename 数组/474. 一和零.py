from typing import List


# 背包问题详解https://leetcode.cn/problems/coin-change/solution/yi-pian-wen-zhang-chi-tou-bei-bao-wen-ti-sq9n/
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        # dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        #
        # for i in range(len(strs)):
        #     zeros = strs[i].count("0")
        #     ones = strs[i].count("1")
        #     for j in range(m, zeros - 1, -1):
        #         for k in range(n, ones - 1, -1):
        #             dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + len(strs[i]))
        # print(dp)
        # return dp[m][n]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        target_0 = m
        target_1 = n
        for s in strs:
            for i in range(target_0, -1, -1):
                for j in range(target_1, -1, -1):
                    if i >= s.count("0") and j >= s.count("1"):
                        dp[i][j] = max(dp[i][j], dp[i - s.count("0")][j - s.count("1")] + 1)
                        # dp[i] = max/min(dp[i], dp[i-num]+nums)
        return dp[m][n]


if __name__ == '__main__':
    res = Solution()
    print(res.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
