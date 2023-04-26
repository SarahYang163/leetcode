import collections
from collections import deque
from typing import List


# 时间O(n)求出在一个数组中，寻找下一个更大的值和前一个更大的值
# [2,3,5,1,6]
# 2左边最大null，右边最大3
# 3左边null，右边5
# 5左边null，右边6
# 1左边5，右边6
# 6左边null，右边null

class Solution:

    def monotonStack(self, arr: List) -> List:
        res = []
        helpStack = []
        for i in range(len(arr)):
            res.append([i, None, None])  # 遍历每个元素时先在结果中加入
            # 如果栈顶元素小于当前元素，应该弹出栈顶元素，当前元素是栈顶元素的下一个最大值，结果记录
            while len(helpStack) != 0 and helpStack[-1][1] < arr[i]:
                tmp = helpStack.pop()
                for t in tmp[0]:
                    res[t][2] = arr[i]  # 当前元素是栈顶元素的下一个最大值
            if len(helpStack) != 0 and helpStack[-1][1] > arr[i]:  # 如果栈顶元素大于当前元素，栈顶元素为当前元素左边最大值，结果记录，并入栈
                res[i][1] = helpStack[-1][1]
                helpStack.append([[i], arr[i]])
            elif len(helpStack) != 0 and helpStack[-1][1] == arr[i]:
                helpStack[-1][0] = helpStack[-1][0] + [i]  # 当前索引加到栈顶的索引
                res[i][1] = res[helpStack[-1][0][0]][1]  # 当前的元素的前一个最大值等于栈顶元素最大值
            else:
                helpStack.append([[i], arr[i]])
        return res


if __name__ == '__main__':
    res = Solution()
    # print(res.monotonStack(
    #     [3, 5, 2, 4, 6, 0, 1, 5]) == [[0, None, 5], [1, None, 6], [2, 5, 4], [3, 5, 6], [4, None, None], [5, 6, 1],
    #                                   [6, 6, 5], [7, 6, None]])
    # print(res.monotonStack(
    #     [3, 5, 5, 5, 1]) == [[0, None, 5], [1, None, None], [2, None, None], [3, None, None], [4, 5, None]])
    #
    # print(res.monotonStack([2, 3, 5, 1, 6]) == [[0, None, 3], [1, None, 5], [2, None, 6], [3, 5, 6], [4, None, None]])
    print(res.monotonStack([1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 3]))
