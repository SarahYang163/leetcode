# https://leetcode.cn/problems/string-compression/
from typing import List


# 输入：chars = ["a","a","b","b","c","c","c"]
# 输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
# 解释："aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。

class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        helpMap = {}
        for i in range(len(chars)):
            if len(helpMap) == 0:
                helpMap[chars[i]] = 1
            elif i != 0 and chars[i] == chars[i - 1]:
                helpMap[chars[i]] = helpMap.get(chars[i]) + 1
            else:
                res.append(chars[i - 1])
                x = helpMap.get(chars[i - 1])
                while x != 0:
                    if int(x / 10) != 0:
                        res.append(str(int(x / 10)))
                    else:
                        res.append(str(x % 10))
                        break
                    x = x % 10
                helpMap.clear()
                helpMap[chars[i]] = 1
        res.append(chars[i - 1])
        x = helpMap.get(chars[i])
        while x != 0:
            if int(x / 10) != 0:
                res.append(str(int(x / 10)))
            else:
                res.append(str(x % 10))
                break
            x = x % 10
        chars = res
        return len(res)


if __name__ == '__main__':
    res = Solution()
    print(res.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
