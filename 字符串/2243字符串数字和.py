class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        p = 0
        s_tmp = ""
        for i in range(len(s)):
            p += int(s[i])
            if (i + 1) % k == 0 or i == len(s) - 1:
                s_tmp = s_tmp + "".join(str(p))
                p = 0
        return self.digitSum(s_tmp, k)


if __name__ == '__main__':
    # res = Solution()
    # print(res.digitSum("1233", 2))
    print(2**100)