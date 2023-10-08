import sys
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        min_ = intervals[0][0]
        max_ = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > max_:
                res.append([min_, max_])
                min_ = intervals[i][0]
                max_ = intervals[i][1]
            elif intervals[i][0] <= max_ and intervals[i][1] > max_:
                max_ = intervals[i][1]
            else:
                pass
        return res
