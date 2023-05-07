# 输入：stones = [2,7,4,1,8,1]
# 输出：1
# 解释：
# 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
# 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
# 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
# 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum = 0
        for i in range(len(stones)):
            sum += stones[i]
        target = int(sum / 2)
        #  定义一维数组dp，表示背包容量是否能够达成
        dp = [False for i in range(target + 1)]
        # // 初始化dp[0]为true
        dp[0] = True
        for i in range(len(stones)):  # 遍历所有石头
            for j in range(target, stones[i] - 1, -1):  # 将当前石头放入容量为 j 的背包中
                dp[j] |= dp[j - stones[i]]  # 如果当前背包能够放下当前石头，则将 dp[j] 的值置为 true
                print(f"dp[j]:", dp[j], " j:", j, " i:", i, " dp:", dp)
        for i in range(target, -1, -1):  # 找到 dp 数组中最接近 sum / 2 的值 i
            if dp[i]:
                return sum - i * 2  # 剩余的石头重量即为 sum - 2 * i
        return -1  # 返回 -1，表示没有符合条件的解


if __name__ == '__main__':
    res = Solution()
    print(res.lastStoneWeightII([2, 3, 4, 1, 5, 1]))
