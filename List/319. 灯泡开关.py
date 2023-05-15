# https://leetcode.cn/problems/bulb-switcher/
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n <= 1:
            return n
        count = 0
        i = 1
        last = 1
        while count < n:
            now = last + 2
            count += now
            i += 1
            last = now
        return i - 1
