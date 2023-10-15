from typing import List


# https://leetcode.cn/problems/subsets/

class Solution:
    def subsets(self, array: List[int]) -> List[List[int]]:
        res = []

        def printallsub(arr: List, i: int, tmp: List) -> str:
            if len(arr) == i:
                res.append(tmp)
                return
            printallsub(arr, i + 1, tmp + [arr[i]])
            printallsub(arr, i + 1, tmp)

        printallsub(array, 0, [])
        return res

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def process(nums: List[int], tmp: List):
            if not nums:
                self.res.append(tmp)
                return
            for i in range(len(nums)):
                process(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        process(nums, [])
        return self.res


if __name__ == '__main__':
    res = Solution()
    print(res.subsets1(["a","c","b"]))
