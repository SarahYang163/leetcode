import collections
import heapq
from typing import List


# 输入：tasks = ["A", "A", "A", "B", "B", "B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
# 在本示例中，两个相同类型任务之间必须间隔长度为
# n = 2
# 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
#
# 链接：https: // leetcode.cn / problems / task - scheduler
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = [0] * 26
        for c in tasks:
            cnts[ord(c) - ord('A')] += 1
        maxv, tot = 0, 0
        for i in range(26):
            maxv = max(maxv, cnts[i])
        for i in range(26):
            tot += 1 if maxv == cnts[i] else 0
        return max(len(tasks), (n + 1) * (maxv - 1) + tot)


if __name__ == '__main__':
    res = Solution()
    print(res.leastInterval(["B", "B", "C", "D", "A", "A", "A", "A", "A", "A", "B", "E", "F", "G"]
                            , 1))
