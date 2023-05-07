from typing import List

#背包问题详解https://leetcode.cn/problems/coin-change/solution/yi-pian-wen-zhang-chi-tou-bei-bao-wen-ti-sq9n/
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(len(strs)):
            zeros = strs[i].count("0")
            ones = strs[i].count("1")
            for j in range(m, zeros-1, -1):
                for k in range(n, ones-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + len(strs[i]))
        print(dp)
        return dp[m][n]


if __name__ == '__main__':
    res = Solution()
    print(res.findMaxForm(["10", "0", "1"], 1, 1))
