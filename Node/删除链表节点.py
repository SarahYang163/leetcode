# Definition for singly-linked list.
import sys
from typing import Optional, List


class ListNode:
    def __init__(self, val: int, next: None):
        self.val = val
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(0)
        pre = res
        pre.next = head
        while head:
            if head.val == val:
                pre.next = head.next
                return res.next
            else:
                pre = pre.next
                head = head.next
        return None

    def removeNodes(self, arr: list) -> list:
        temp = arr[::-1]
        res = []
        under = 0
        for t in temp:
            if t > under:
                res.append(t)
                under = t
        return res[::-1]

    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):
            count_0 = 0
            while i < len(s) and s[i] == "0":
                count_0 += 1
                i += 1
            count_1 = 0
            while i < len(s) and s[i] == "1":
                count_1 += 1
                i += 1
            res = max(res, min(count_0, count_1))
        return res

    def greatestLetter(self, s: str) -> str:
        s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s1 = s1[::-1]
        for c in s1:
            if c in s and c.lower() in s:
                return c
        return ""

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        # sum_ = 0
        res = sys.maxsize
        while start < len(nums) and end < len(nums):
            sum_ = sum(nums[start:end + 1])
            if sum_ < target:
                end += 1
            else:
                res = min(res, end - start + 1)
                start += 1
        return res

    def longestWord(self, words: List[str]) -> str:
        res = ""
        for word in words:
            i = 1
            while i < len(word) and word[:i] and word[:i] in words:
                i += 1
            if i == len(word):
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):
                    res = word if word < res else res
        return res

    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        i, j = 0, len(grid[0]) - 1
        while i <= len(grid) - 1 and j >= 0:
            if grid[i][j] >= 0:
                i += 1
            else:
                res += len(grid) - i
                j -= 1
        return res

    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        print(num)
        res = 0
        while num != 1:
            res += 1
            if num % 2 == 1:
                num += 1
            else:
                num //= 2
        return res


if __name__ == '__main__':
    res = Solution()
    # print(res.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
    print(res.numSteps("11110111100000111000001100111001010111110001"))
    print(3>>1)
