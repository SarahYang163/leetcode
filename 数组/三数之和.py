from typing import List


# https://leetcode.cn/problems/3sum/

class Solution:
    # 此解法包含重复项
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            target = -nums[i]
            map = {}
            for j in range(i + 1, len(nums)):
                if map.get(target - nums[j]) is not None:
                    res.append([nums[i], nums[j], nums[map.get(target - nums[j])]])
                else:
                    map[nums[j]] = j
        return res

    # 此解法去重之后，可达目的，但是太慢了
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            map = {}
            for j in range(i + 1, len(nums)):
                if map.get(target - nums[j]) is not None:
                    res.append([nums[i], nums[j], nums[map.get(target - nums[j])]])
                else:
                    map[nums[j]] = j
        return [list(i) for i in set(tuple(_) for _ in res)]


if __name__ == '__main__':
    res = Solution()
    print(res.threeSum1([1, 0, -1, 2, -1, -4]))
