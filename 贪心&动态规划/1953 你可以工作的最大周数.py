# https://leetcode.cn/p roblems/maximum-number-of-weeks-for-which-you-can-work/
from typing import List
from queue import PriorityQueue


class Solution:
    # 超时算法
    def numberOfWeeks(self, milestones: List[int]) -> int:
        res = 0
        pq = PriorityQueue()
        last_pop_num = 0
        for a in milestones:
            pq.put((-a, a))
        while pq.qsize() >= 1:
            res += 1
            now_pop_num = pq.get()[1]
            if last_pop_num > 1:
                pq.put((-(last_pop_num - 1), (last_pop_num - 1)))
            last_pop_num = now_pop_num
        return res

    # 不超时算法
    def numberOfWeeks1(self, milestones: List[int]) -> int:
        sumNum, maxNum = 0, 0
        for a in milestones:
            sumNum += a
            maxNum = max(maxNum, a)
        if maxNum > sumNum / 2:
            return (sumNum - maxNum) * 2 + 1
        return sumNum


if __name__ == '__main__':
    arr = [723, 651, 790, 980, 51, 242, 386, 581, 225, 970, 341, 239, 425, 486, 498, 717, 521, 12, 177, 49, 480, 749,
           161, 714, 344, 758, 858, 913, 216, 132, 851, 420, 945, 2, 45, 140, 647, 774, 786, 129, 514, 336, 602, 485,
           130, 939, 271, 546, 56, 943, 118, 603, 926, 296, 929, 696, 724, 510, 965, 614, 342, 211, 960, 572, 897, 141,
           114, 919, 259, 538, 422, 464, 675, 388, 37, 975, 392, 393, 621, 227, 428, 794, 986, 934, 892, 317, 790, 633,
           197, 95, 269, 111, 830, 149, 923, 531, 42, 558, 903, 868, 431, 306, 467, 541, 113, 531, 839, 562, 831, 148,
           835, 701, 105, 624, 28, 578, 920, 849, 498, 176, 335, 148, 481, 359, 793, 34, 342, 537, 153, 830, 76, 239,
           679, 749, 109, 954, 893, 682, 884, 109, 265, 18, 812, 443, 552, 744, 929, 968, 322, 452, 951, 206, 253, 835,
           63, 58, 889, 858, 918, 541, 352, 767, 12, 614, 804, 450, 689, 372, 966, 101, 863, 27, 177, 329, 324, 578, 26,
           960, 892, 194, 948, 367, 170, 854, 838, 674, 115, 188, 821, 117328, 790, 684, 872, 379, 684, 805, 962, 836,
           419, 748, 964, 276, 105, 679, 868, 490, 389, 443, 742, 114, 558, 310, 461, 137, 566, 361, 207, 851, 787, 96,
           356, 510, 725, 573, 524, 438, 311, 201, 959]
    res = Solution()
    print(res.numberOfWeeks(arr))
    pq = PriorityQueue()
    for a in arr:
        pq.put((-a, a))
    print(pq.get()[1])
    # heapq.heapify(arr*(-1))
    # pq.put(3)
    print(arr)
    print(f"move", arr[0], "to", arr[1])
