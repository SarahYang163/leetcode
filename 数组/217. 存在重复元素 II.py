# https://leetcode.cn/problems/contains-duplicate-ii/

# 输入：nums = [1,2,3,1], k = 3
# 输出：true
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 字典解法
        # map = {}
        # for i in range(len(nums)):
        #     if map.get(nums[i]) is not None and abs(map.get(nums[i]) - i) <= k:
        #         return True
        #     map[nums[i]] = i
        # return False

        # 滑动窗口+集合做法
        helpSet = set()
        for r in range(len(nums)):
            if r > k:
                helpSet.remove(nums[r - k - 1])

            if nums[r] in helpSet:
                return True
            helpSet.add(nums[r])
        return False


if __name__ == '__main__':
    res = Solution()
    print(res.containsNearbyDuplicate([1], 1))
