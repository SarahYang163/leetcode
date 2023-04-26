class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        l = len(s)
        for i in range(l - 2, -1, -1):
            if s[i] < s[i + 1]:
                while l - 1 >= i + 1 and s[l - 1] <= s[i]:
                    l -= 1
                tmp = s[i]
                s[i] = s[l - 1]
                s[l - 1] = tmp
                s[i + 1:] = sorted(s[i + 1:])
                return int("".join(s)) if int("".join(s)) <= 2 ** 31 - 1 else -1
        return -1


if __name__ == '__main__':
    s = "APPLE"
    a = 2 ** 31 - 1
    print(a)
