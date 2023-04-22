# 一个牛一年生1头小母牛，小母牛三年后才可以再生，假设牛不会死，N年后有多少牛

def count(N: int) -> int:
    if 0 < N <= 4:
        return N
    return count(N - 1) + count(N - 3)


# 一个牛一年生1头小母牛，小母牛三年后才可以再生，假设牛10年后会死，N年后有多少牛
def count1(N: int) -> int:
    if N < 0:
        return 0
    elif 0 < N <= 4:
        return N
    else:
        return count1(N - 1) + count1(N - 3) - count1(N - 10)


if __name__ == '__main__':
    print(count(11))
    print(count1(11))
