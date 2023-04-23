from typing import List


# 判断字符串str2是否是str1的子串，返回第一个字符的位置，不是返回-1
def kmp(str1: str, str2: str) -> int:
    if len(str1) < 1 or len(str2) < 1 or len(str2) > len(str1):
        return -1
    i = 0
    j = 0
    next_arr = findNext(str2)
    while j < len(str2) and i < len(str1):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            if next_arr[j] == -1:
                i += 1
            else:
                j = next_arr[j]

    return i - j if j == len(str2) else -1


# 找到一个数组的最长 前缀和后缀匹配
def findNext(s: str) -> List:
    n = len(s)
    next_arr = [None] * n
    next_arr[0] = -1
    if n == 1:
        return next_arr
    next_arr[1] = 0
    if n == 2:
        return next_arr
    i = 2
    cn = 0
    while i < n:
        if s[i - 1] == s[cn]:
            next_arr[i] = cn + 1
            i += 1
            cn += 1
        elif cn > 0:
            cn = next_arr[cn]
        else:
            next_arr[i] = 0
            i += 1
    return next_arr


if __name__ == '__main__':
    print(kmp("leetcode", "leeto"))
