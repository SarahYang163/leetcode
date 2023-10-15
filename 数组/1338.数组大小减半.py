# 输入：arr = [3,3,3,3,5,5,5,2,2,7]
# 输出：2
# 解释：选择 {3,7} 使得结果数组为 [5,5,5,2,2]、长度为 5（原数组长度的一半）。
# 大小为 2 的可行集合有 {3,5},{3,2},{5,2}。
# 选择 {2,7} 是不可行的，它的结果数组为 [3,3,3,3,5,5,5]，新数组长度大于原数组的二分之一。
import collections
from typing import List


class Solution:
    # 忘了用计数器了呜呜呜，还在傻傻的用map
    def minSetSize(self, arr: List[int]) -> int:
        map_ = {}
        for a in arr:
            if a not in map_:
                map_[a] = 1
            else:
                map_[a] += 1
        arrHelp = sorted(map_.items(), key=lambda x: (-x[1], x[0]))
        k = len(arr) >> 1
        i = 0
        res = 0
        print(arrHelp)
        while k > 0:
            k -= arrHelp[i][1]
            i += 1
            res += 1
        return res

        # 计数器做法

    def minSetSize1(self, arr: List[int]) -> int:
        freq = collections.Counter(arr)
        cnt, ans = 0, 0
        for num, occ in freq.most_common():
            cnt += occ
            ans += 1
            if cnt * 2 >= len(arr):
                break
        return ans


if __name__ == '__main__':
    res = Solution()
    print(res.minSetSize1([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
