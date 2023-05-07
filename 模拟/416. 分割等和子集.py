from typing import List
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# https://leetcode.cn/problems/partition-equal-subset-sum/
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum=0
        for num in nums:
            sum+=num
        if sum%2==1:
            return False
        target=sum>>1
        dp=[False for _ in range(target+1)]
        dp[0]=True
        for num in nums:
            for i in range(target,num-1,-1):
                dp[i]|=dp[i-num]
        print(dp)
        return dp[target]
