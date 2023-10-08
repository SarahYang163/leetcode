# https://leetcode.cn/problems/integer-break/
# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
# 返回 你可以获得的最大乘积 。
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n):  # nums
            for j in range(i, n + 1):  # target
                dp[j] = max(dp[j], dp[j - i] * i, (j - i) * i)
        return dp[n]

if __name__ == '__main__':
    res = Solution()
    print(res.integerBreak(4))
