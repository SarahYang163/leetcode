from typing import List


class Soluction:
    def QKSourt(self, a: List, start: int, end: int):
        if len(a) < 0:
            return
        if start >= end:
            return
        left = start
        right = end
        temp = a[left]
        while left < right:
            while left < right and a[right] >= temp:
                right -= 1

            a[left] = a[right]
            while left < right and a[left] <= temp:
                left += 1

            a[right] = a[left]

        a[left] = temp
        print(a)
        self.QKSourt(a, start, left - 1)
        self.QKSourt(a, left + 1, end)


if __name__ == '__main__':
    a = [5, 16, 4, 8, 36, 13, 44]
    res = Soluction()
    res.QKSourt(a, 0, len(a) - 1)
    print(a)
