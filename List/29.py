# def divide(self, dividend: int, divisor: int) -> int:
#     flag = False
#     if dividend & divisor:
#         flag = True
#     cnt = 0
#     tmp_divisor = abs(divisor)
#     dividend = abs(dividend)
#     while 1:
#         if tmp_divisor <= dividend:
#             cnt = cnt + 1
#             tmp_divisor = tmp_divisor + divisor
#         else:
#             break
#     return cnt if flag is True else -cnt
from typing import List


def isValid(s: str) -> bool:
    map_ = {}
    arr = []
    map_[")"] = "("
    map_["}"] = "{"
    map_["]"] = "["
    for c in s:
        if c in map_.values():
            arr.append(c)
        else:
            if len(arr) == 0:
                return False
            else:
                if arr[-1] is map_[c]:
                    arr.pop()
                else:
                    return False
    return True if len(arr) == 0 else False


if __name__ == '__main__':
    def divide(dividend: int, divisor: int) -> int:
        flag = False
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            flag = True
        cnt = 0
        tmp_divisor = abs(divisor)
        tmp = tmp_divisor
        dividend = abs(dividend)
        while 1:
            if tmp <= dividend:
                cnt = cnt + 1
                tmp = tmp + tmp_divisor
            else:
                break
        return cnt if flag is True else -cnt


    def truncateSentence(s: str, k: int) -> str:
        arr = s.split(' ')
        s_tmp = arr[0]
        for i in range(1, k):
            s_tmp = s_tmp + " " + arr[i]
        return s_tmp


    def longestSquareStreak(nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        max_ = 0
        for num in nums:
            num_2 = num ** 2
            cnt = 0
            while num_2 in nums:
                cnt = cnt + 1
                nums.remove(num_2)
                num_2 = num_2 ** 2

            max_ = max(max_, cnt)
        return max_


    print(isValid("]"))
