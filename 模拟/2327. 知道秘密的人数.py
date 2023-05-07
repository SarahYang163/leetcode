# https://leetcode.cn/problems/number-of-people-aware-of-a-secret/
# 输入：n = 6, delay = 2, forget = 4
# 输出：5
# 解释：
# 第 1 天：假设第一个人叫 A 。（一个人知道秘密）
# 第 2 天：A 是唯一一个知道秘密的人。（一个人知道秘密）
# 第 3 天：A 把秘密分享给 B 。（两个人知道秘密）
# 第 4 天：A 把秘密分享给一个新的人 C 。（三个人知道秘密）
# 第 5 天：A 忘记了秘密，B 把秘密分享给一个新的人 D 。（三个人知道秘密）
# 第 6 天：B 把秘密分享给 E，C 把秘密分享给 F 。（五个人知道秘密）


# 空间换时间做法，用一个数组记录之前的结果，每个if都是推算出来的
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        helpArr = [0 for i in range(n)]
        i = 0
        while i < n:
            if i < delay:
                helpArr[i] = 1
            elif i < forget:
                helpArr[i] = helpArr[i - 1] + helpArr[i - delay]
            elif i == forget:
                helpArr[i] = helpArr[i - 1] + helpArr[i - delay] - 2 * helpArr[i - forget]
            else:
                helpArr[i] = helpArr[i - 1] + helpArr[i - delay] - helpArr[i - forget]
            i += 1
        return helpArr[n - 1] % (10 ** 9 + 7)
    # 递归做法---严重超时
    # def peopleAwareOfSecret(self, N: int, delay: int, forget: int) -> int:
    #     if N <= 0:
    #         return 0
    #     elif N <= delay:
    #         return 1
    #     elif N == forget + 1:
    #         return (self.peopleAwareOfSecret(N - 1, delay, forget) + self.peopleAwareOfSecret(N - delay, delay,
    #                                                                                           forget) - 2 * self.peopleAwareOfSecret(
    #             N - forget, delay, forget)) % (10 ** 9 + 7)
    #     else:
    #         return (self.peopleAwareOfSecret(N - 1, delay, forget) + self.peopleAwareOfSecret(N - delay, delay,
    #                                                                                           forget) - self.peopleAwareOfSecret(
    #             N - forget, delay, forget)) % (10 ** 9 + 7)
