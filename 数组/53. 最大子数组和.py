# https://leetcode.cn/problems/maximum-subarray/
import collections
import sys
from typing import List, Optional

from Node.二叉树中的前驱节点 import TreeNode


class Solution:
    # 超时辣，因为时间复杂度O(n*n)
    # def maxSubArray(self, nums: List[int]) -> int:
    #     result = -sys.maxsize - 1
    #     l = 0
    #     while l < len(nums):
    #         r = l
    #         sunNum = 0
    #         while r < len(nums):
    #             sunNum += nums[r]
    #             result = max(result, sunNum)
    #             if sunNum <= 0:
    #                 break
    #             r += 1
    #         l += 1
    #     return result
    # 动态规划
    # f(i)=max{f(i−1)+nums[i],nums[i]}
    def maxSubArray(self, nums: List[int]) -> int:
        result = -sys.maxsize - 1
        l, pre = 0, -sys.maxsize - 1
        while l < len(nums):
            pre = max(pre + nums[l], nums[l])
            result = max(result, pre)
            l += 1
        return result

    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        res = ''
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            while l >= 0 and s[l] == s[i]:
                l = l - 1
            while r < len(s) and s[r] == s[i]:
                r = r + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l + 1 > max_len:
                res = s[l + 1:r]
                max_len = r - l + 1
        return res

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        res = 1
        i = 0
        while i < n - 1:
            j = i
            while i < n - 1 and nums[i + 1] - nums[i] == 1:
                i += 1
            res = max(res, i - j + 1)
            i += 1
        return res

    def findDuplicate(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        print(freq.pop())
        return freq.most_common(1)

        # 输入：nums = [5,7,7,8,8,10], target = 6
        # 输出：[-1,-1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                print(mid)
                left, right = mid, mid
                while left - 1 >= 0 and nums[left - 1] == nums[mid]:
                    left -= 1
                while right + 1 < len(nums) and nums[right + 1] == nums[mid]:
                    right += 1
                return [left, right]
        return [-1, -1]

    def lengthOfLongestSubstring(self, s: str) -> int:

        # map_ = {}
        # start = 0
        # max_len = 1
        # i = 0
        # while i < len(s):
        #     if s[i] not in map_.keys():
        #         map_[s[i]] = i
        #         max_len = max(max_len, i - start + 1)
        #         i+=1
        #     else:
        #         max_len = max(max_len, i - start)
        #         start = map_[s[i]] + 1
        #         map_.clear()
        #         i = start
        # return max_len
        map1 = dict()
        length = 0
        p = 0
        if len(s) <= 1:
            return len(s)
        for i in range(len(s)):
            if map1.get(s[i], -1) != -1:
                p = max(map1.get(s[i]) + 1, p)
            length = max(length, i - p + 1)
            map1[s[i]] = i
        return length

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        print("1")
        return self.isValidBST2(root, -sys.maxsize + 1, sys.maxsize)

    def isValidBST2(self, root: Optional[TreeNode], min_num: int, max_num: int) -> bool:
        print("1")
        if root is None:
            return True
        if max_num > root.val > min_num:
            pass
        else:
            return False
        return self.isValidBST2(root.left, min_num, root.val) and self.isValidBST2(root.right, root.val,
                                                                                   max_num)

    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:].startswith(needle):
                return i
        return -1

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def process(nums: List[int], tmp: List[int]):
            if len(nums) == 0:
                return res.append(tmp)
            process(nums[1:], tmp + [])
            process(nums[1:], tmp)

        process(nums, [])
        return res

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1 = nums2
        l = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[l] = nums1[m - 1]
                m -= 1
            else:
                nums1[l] = nums2[n - 1]
                n -= 1
            l -= 1
        print(nums1)
        return


if __name__ == '__main__':
    res = Solution()
    print(res.merge([0], 0, [1], 1))
