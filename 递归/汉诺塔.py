from typing import List


class Solution:
    def move(self, n, From: List[int], help: List[int], to: List[int]) -> None:
        if n == 1:
            to.append(From.pop())
        else:
            self.move(n - 1, From, to, help)
            to.append(From.pop())
            self.move(n - 1, help, From, to)

    def hanota(self, From: List[int], help: List[int], to: List[int]) -> List:
        """
        Do not return anything, modify C in-place instead.
         """
        n = len(From)
        self.move(n, From, help, to)
        return to



if __name__ == '__main__':
    res = Solution()
    print(res.hanota([3,2,1], [], []))
