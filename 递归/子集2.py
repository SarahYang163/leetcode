from typing import List


class Solution:
    def subsetsWithDup(self, array: List[int]) -> List[List[int]]:
        res = []
        array.sort()

        def printallsub(arr: List, i: int, tmp: List):
            if len(arr) == i:
                if tmp not in res:
                    res.append(tmp)
                return
            printallsub(arr, i + 1, tmp + [arr[i]])
            printallsub(arr, i + 1, tmp)

        printallsub(array, 0, [])

        return res
        # res.sort(key=res.index)
        # [list(t) for t in set(tuple(_) for _ in res)]


if __name__ == '__main__':
    res = Solution()
    print(res.subsetsWithDup([4, 4, 4, 1, 4]))
    b = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    apple = [list(a) for a in (set(tuple(_) for _ in b))]
    # b = [list(t) for t in set(tuple(_) for _ in b)]
    print()
