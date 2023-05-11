from typing import List


class Solution:
    # 输入：nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
    # 输出：19
    # 解释：一个可行的 nums 排列为 [2,1,3,4,5]，并有如下结果：
    # requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
    # requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
    # 总和为：8 + 3 = 11。
    # 一个总和更大的排列为 [3,5,4,2,1]，并有如下结果：
    # requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
    # requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
    # 总和为： 11 + 8 = 19，这个方案是所有排列中查询之和最大的结果。
    #
    # https://leetcode.cn/problems/maximum-sum-obtained-of-any-permutation/

    # 求出每个元素要计算的次数 然后从大到小排就好了 把最大的元素赋值给最多的元素就好了

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        res = 0
        # 求出每个元素要计算的次数 然后从大到小排就好了 把最大的元素赋值给最多的元素就好了
        n = len(nums)
        countArr = [0 for _ in range(n + 1)]
        for request in requests:
            countArr[request[0]] += 1
            countArr[request[1] + 1] -= 1
        # 只需要到n
        count = [0 for _ in range(n)]
        count[0] = countArr[0]
        for i in range(1, n):
            count[i] = count[i - 1] + countArr[i]
        # 如果要求输出的是符合要求的数组
        # count_zip = list(zip(count, [i for i in range(n)]))
        # count_zip.sort(key=lambda x: x[0])
        # res_arr = [0 for _ in range(n)]
        # nums.sort()
        # for i in range(n):
        #     res_arr[count_zip[i][1]] = nums[i]
        # print(res_arr)

        count.sort()
        nums.sort()
        for j in range(n):
            res += nums[j] * count[j]
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    demo = Solution()
    print(demo.maxSumRangeQuery([1, 2, 3, 4, 5], [[1, 3], [0, 1]]))
