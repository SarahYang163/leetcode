# https://leetcode.cn/problems/next-permutation/
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        i = n - 2
        while i >= 0:#遍历到第一个索引
            if nums[i] < nums[i + 1]:#有升序数对存在
                while nums[n-1]<=nums[i]:#从最后开始找，找到大于当前值的索引n-1
                    n-=1
                #i 和n-1 交换
                tmp = nums[i]
                nums[i] = nums[n - 1]
                nums[n - 1] = tmp
                #剩余数字从大到小排序
                nums[i + 1:] = sorted(nums[i + 1:])
                return
            i -= 1
        #如果都到第一个数字都没匹配，没有升序数对，返回最小数列
        if i < 0:
            nums.sort()
            return


if __name__ == '__main__':
    array = [1, 2, 7, 6, 5, 4, 3]
    res = Solution()
    res.nextPermutation(array)
    # res = array[:3] + sorted(array[3::1])
    print(array)
