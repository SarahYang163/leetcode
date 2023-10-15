import heapq
import queue


# from queue import PriorityQueue, Queue


class Solution:

    def halveArray(self, nums: list) -> int:
        sum_ = sum(nums) / 2
        print(sum_)
        count = 0
        nums = [_ * (-1) for _ in nums]
        heapq.heapify(nums)
        while -sum(nums) >= sum_:
            count += 1
            temp = heapq.heappop(nums)
            heapq.heappush(nums, temp / 2)
        return count


if __name__ == '__main__':
    res = Solution()
    print(res.halveArray([5,19,8,1]))
