def manacherString(s: str) -> str:
    if len(s) < 1:
        return s
    res = ""
    for c in s:
        res = res + "#" + c
    res += "#"
    return res


# 查找一个字符串中的最长回文子串
def manacherlength(s: str) -> str:
    s = manacherString(s)
    n = len(s)
    max_l, i, max_l_index, res = -1, 0, 0, ""
    arr_redius = [0] * n  # 记录每个位置的回文半径
    while i < n:
        if i >= max_l:
            x = 1
            while i - x >= 0 and i + x < n and s[i - x] == s[i + x]:
                x += 1
            if i + x - 1 > max_l:
                max_l = i + x - 1  # 回文半径到达最远时的地址
                max_l_index = i  # 回文半径到达最远时的中心位置
            arr_redius[i] = x - 1
        else:
            if (2 * max_l_index - i) - arr_redius[2 * max_l_index - i] > 2 * max_l_index - max_l:
                arr_redius[i] = arr_redius[2 * max_l_index - i]
            elif (2 * max_l_index - i) - arr_redius[2 * max_l_index - i] < 2 * max_l_index - max_l:
                arr_redius[i] = max_l - i
            else:
                x = i - max_l_index + 1
                while i - x >= 0 and i + x < n and s[i - x] == s[i + x]:
                    x += 1
                arr_redius[i] = x - 1
                if x > arr_redius[max_l_index]:
                    max_l = i + x
                    max_l_index = i
        if 2 * arr_redius[i] + 1 > len(res):
            res = s[2 * max_l_index - max_l:max_l + 1]
        i += 1
    res = res.split("#")
    return "".join(res[1:len(res) - 1])


if __name__ == '__main__':
    # res = manacherlength("abccba").split('#')
    print(manacherlength("ccc"))
