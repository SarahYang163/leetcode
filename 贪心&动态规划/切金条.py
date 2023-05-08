# 1、题目描述
# 一块金条切成两半，是需要花费和长度数值一样的铜板的。比如长度为20的金条，不管怎么切，都要花费20个铜板。一群人想整分整块金条，怎么分最省铜板？输入一个数组，返回分割的最小代价。
#
# 例如：
#
# 给定数组{10,20,30}，代表一共三个人， 整块金条长度为10 + 20 + 30 = 60，金条要分成10, 20, 30三个部分（不考虑顺序）。
#
# 如果先把长度60的金条分成10和50，花费60；再把长度50的金条分成20和30，花费50;一共花费110铜板。
#
# 但如果先把长度60的金条分成30和30，花费60；再把长度30金条分成10和20，花费30；一共花费90铜板。
from queue import PriorityQueue

from typing import List


class Solution:
    def minGoldCost(self, cuts: List[int]) -> int:
        cuts.sort()
        pq = PriorityQueue()  # 优先级队列
        ans = 0
        for cut in cuts:
            pq.put(cut)
        while pq.qsize() > 1:
            ans = pq.get() + pq.get()
            pq.put(ans)
        return ans


if __name__ == '__main__':
    ans = Solution()
    print(ans.minGoldCost([1, 2, 6, 4, 3, 7, 1, 8]))
