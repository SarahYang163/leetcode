# https://leetcode.cn/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_tmp = []
        for c in s:
            if c.isdigit() or c.islower():
                s_tmp.append(c)
            elif c.isupper():
                s_tmp.append(c.lower())
        return "".join(s_tmp) == "".join(s_tmp[len(s_tmp) - 1::-1])


if __name__ == '__main__':
    # res = Solution()
    # print(res.isPalindrome("A man, a plan, a canal: Panama"))
    # print(res.isPalindrome("race a car"))
    # print(res.isPalindrome("a7,g7a "))
    #不用字符串解法
    x = 1221
    yushu = 0
    x1 = x
    while x / 10 != 0:
        yushu = yushu * 10 + int(x % 10)
        x = int(x / 10)
        print(yushu)
    print(x1 == yushu)
