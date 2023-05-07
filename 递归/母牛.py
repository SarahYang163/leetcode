# 一个牛一年生1头小母牛，小母牛三年后才可以再生，假设牛不会死，N年后有多少牛

def count(N: int) -> int:
    if 0 < N <= 4:
        return N
    return count(N - 1) + count(N - 3)


# 一个牛一年生1头小母牛，小母牛三年后才可以再生，假设牛10年后会死，N年后有多少牛
def count1(N: int) -> int:
    if N <= 0:
        return 0
    elif N <= 2:
        return 1
    elif N == 5:
        return count1(N - 1) + count1(N - 2) - 2 * count1(N - 4)
    else:
        return count1(N - 1) + count1(N - 2) - count1(N - 4)


class Solution:
    def peopleAwareOfSecret(self, N: int, delay: int, forget: int) -> int:
        if N <= 0:
            return 0
        elif N <= delay:
            return 1
        elif N == forget + 1:
            return (self.peopleAwareOfSecret(N - 1, delay, forget) + self.peopleAwareOfSecret(N - delay, delay,
                                                                                              forget) - 2 * self.peopleAwareOfSecret(
                N - forget, delay, forget)) % (10 ** 9 + 7)
        else:
            return (self.peopleAwareOfSecret(N - 1, delay, forget) + self.peopleAwareOfSecret(N - delay, delay,
                                                                                              forget) - self.peopleAwareOfSecret(
                N - forget, delay, forget)) % (10 ** 9 + 7)


if __name__ == '__main__':
    # print(count(11))
    # print(count1(6))
    res = Solution()
    print(res.peopleAwareOfSecret(684, 18, 496))
