import string
from collections import Counter
from typing import List


class Soluction:
    def top_n_big(self, arr: list, n: int):
        if n > len(arr) or n <= 0:
            return None
        for i in range(n):
            for j in range(i + 1, len(arr)):
                if arr[j] > arr[i]:
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
        return arr[n - 1]

    def top_n_big_2(self, arr: list, n: int):
        if n > len(arr) or n <= 0:
            return None
        arr.sort()
        return arr[len(arr) - n]

    def feibonaqie(self, n: int):
        if n <= 0:
            return None
        elif n == 1 or n == 2:
            return 1
        return self.feibonaqie(n - 1) + self.feibonaqie(n - 2)

    # 给定一个字符串，要求输出新字符串不含驼峰。input：abcdAFAe ， output ：abcde。驼峰含义：如AFA、AFFA、afa、affa
    def test(self, s: string):
        res = []
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub_s = s[i:j]
                if not sub_s == sub_s[::-1]:
                    res.append(sub_s)
        return "".join(res)

    def is_palindrome(self, s):

        return s == s[::-1]

    def remove_palindromes(self, string):

        longest_palindrome = ""
        longest_length = 0
        n = len(string)

        for i in range(n):
            for j in range(i + 1, n + 1):
                sub_string = string[i:j]
                if self.is_palindrome(sub_string) and len(sub_string) > longest_length:
                    longest_length = len(sub_string)
                    longest_palindrome = sub_string

        result = string.replace(longest_palindrome, "")
        return result

    def minimumDeletions(self, nums: List[int]):
        n = len(nums)
        res = 0
        max_index = nums.index(max(nums))
        min_index = nums.index(min(nums))
        if max_index >= n >> 1 and min_index >= n >> 1:
            res = n - min(max_index, min_index)
        elif max_index < n >> 1 and min_index < n >> 1:
            res = max(max_index, min_index) + 1
        else:
            res = min(max_index, min_index) + 1 + n - max(max_index, min_index)
        return res

    def stoneGameVII(self, stones: List[int]):
        sum1 = 0
        sum2 = 0
        flag = True
        while stones:
            if flag == True:
                sum_ = sum1
            else:
                sum_ = sum2
            if stones[0] < stones[-1]:
                sum_ += sum(stones[1:])
                stones = stones[1:]
            else:
                sum_ += sum(stones[:-1])
                stones = stones[:-1]
            if flag == True:
                sum1 = sum_
            else:
                sum2 = sum_
            flag = -flag
        return sum1 - sum2

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        s2 = ""
        for w in word1:
            s1 += w
        for w in word2:
            s2 += w
        return s1 == s2


if __name__ == '__main__':
    res = Soluction()
    print(res.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
    # nums1 = [1, 2, 2, 1], nums2 = [2, 2]
    # 输入：nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
