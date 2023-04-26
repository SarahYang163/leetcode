# https://leetcode.cn/problems/daily-temperatures/
from typing import List


# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List:
        res = [0] * len(temperatures)
        helpStack = []
        for i in range(len(temperatures)):
            # res.append([i, None])  # 遍历每个元素时先在结果中加入
            # 如果栈顶元素小于当前元素，应该弹出栈顶元素，当前元素是栈顶元素的下一个最大值，结果记录
            while len(helpStack) != 0 and helpStack[-1][1] < temperatures[i]:
                tmp = helpStack.pop()
                res[tmp[0]] = i - tmp[0]  # 当前元素是栈顶元素的下一个最大值
            helpStack.append([i, temperatures[i]])
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
