from typing import List


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        res = []
        helpMap = {}
        helpMap["2"] = ["a", "b", "c"]
        helpMap["3"] = ["d", "e", "f"]
        helpMap["4"] = ["g", "h", "i"]
        helpMap["5"] = ["j", "k", "l"]
        helpMap["6"] = ["m", "n", "o"]
        helpMap["7"] = ["p", "q", "r", "s"]
        helpMap["8"] = ["t", "u", "v"]
        helpMap["9"] = ["w", "x", "y", "z"]

        n = len(num)
        for word in words:
            flag = True
            if len(word) == n:
                for i in range(len(word)):
                    if word[i] not in helpMap.get(num[i]):
                        flag = False
                        break
            else:
                flag = False
            if flag == True:
                res.append(word)
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.getValidT9Words("2233", ["abee", "usedy", "aafe"]))
