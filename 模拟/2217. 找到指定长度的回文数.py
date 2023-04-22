# https://leetcode.cn/problems/find-palindrome-with-fixed-length/
from typing import List


class Solution:
    def kthPalindrome(self, qs: List[int], k: int) -> List[int]:
        res = []
        max_num = 9 * (10 ** int((k+1) / 2 - 1))
        for q in qs:
            if q > max_num:
                res.append(-1)
            else:
                tmp = 10 ** (int((k + 1) / 2) - 1) + q - 1
                if k % 2 == 0:  # 偶数
                    res.append(int(str(tmp) + str(tmp)[::-1]))
                else:  # 奇数
                    res.append(int(str(tmp) + str(tmp)[:len(str(tmp))-1][::-1]))
        return res


if __name__ == '__main__':
    res = Solution()
    print(res.kthPalindrome([1, 2, 3, 4, 5, 90], 3))
