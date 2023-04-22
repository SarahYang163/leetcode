from typing import List
# https://leetcode.cn/problems/subsets/

class Solution:
    def subsets(self, array: List[int]) -> List[List[int]]:
        res=[]
        def printallsub(arr: List, i: int, tmp: List) -> str:
            if len(arr) == i:
                res.append(tmp)
                return
            printallsub(arr, i + 1, tmp + [arr[i]])
            printallsub(arr, i + 1, tmp)


        printallsub(array, 0, [])
        return res