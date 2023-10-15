from typing import List


# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
#

# 背包类型：组合背包，因为选择ab和ba两个单词的顺序对结果是不一样的
# 问题类型：存在问题
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for j in range(len(s) + 1):
            for word in wordDict:
                if j >= len(word):
                    if s[j - len(word):j] == word:
                        dp[j] |= dp[j - len(word)]
        print(dp)
        return dp[len(s)]


if __name__ == '__main__':
    res = Solution()
    # print(res.wordBreak("bccdbacdbdacddabbaaaadababadad",
    #                     ["cbc", "bcda", "adb", "ddca", "bad", "bbb", "dad", "dac", "ba", "aa", "bd", "abab", "bb",
    #                      "dbda", "cb", "caccc", "d", "dd", "aadb", "cc", "b", "bcc", "bcd", "cd", "cbca", "bbd", "ddd",
    #                      "dabb", "ab", "acd", "a", "bbcc", "cdcbd", "cada", "dbca", "ac", "abacd", "cba", "cdb", "dbac",
    #                      "aada", "cdcda", "cdc", "dbc", "dbcb", "bdb", "ddbdd", "cadaa", "ddbc", "babb"]))
    print(res.wordBreak("catsandog", ["cats", "dog", "san", "and", "cat"]))
