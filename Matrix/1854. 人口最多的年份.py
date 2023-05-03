from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = []
        res = 0
        maxPeopleNum = 0
        currentNum = 0
        for array in logs:
            arr.append([array[1], -1])
        for array in logs:
            arr.append([array[0], 1])
        arr.sort(key=lambda x: x[0])
        for a in arr:
            currentNum += a[1]
            if currentNum > maxPeopleNum:
                maxPeopleNum = currentNum
                res = a[0]
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.maximumPopulation(
        [[2008, 2026], [2004, 2008], [2034, 2035], [1999, 2050], [2049, 2050], [2011, 2035], [1966, 2033],
         [2044, 2049]]))
