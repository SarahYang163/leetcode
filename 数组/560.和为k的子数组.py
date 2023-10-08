from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        sums, res = 0, 0
        for num in nums:
            sums += num
            res += dic.get(k - num, 0)
            dic[num] = dic.get(k - num, 0) + 1
        return res


if __name__ == '__main__':
    arr = [2, 4, 1, 3]
    print(max(arr))
    res = Solution()
    print(res.subarraySum([1, 2, 3, 4, -5, 2, 1, -4, 1, 2, -1, 4, 1, -1, 1, 10, 2], 11))
