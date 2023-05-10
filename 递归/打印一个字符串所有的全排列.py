# 给定一个字符串，打印他所有的全排列
from typing import List


class Solution:
    res = []
    def permute(self, nums: List[int]) -> List[List[int]]:


        # def backtrack(nums, tmp):
        #     if not nums:
        #         self.res.append(tmp)
        #         return
        #     for i in range(len(nums)):
        #         backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])
        #
        # backtrack(nums, [])
        return self.res


if __name__ == '__main__':
    res = Solution()
    arr = [1, 4, 2]
    print(res.permute(arr))
    # l = [2, 6, 9]
    # print(arr + l)
    # print(arr[5:])
