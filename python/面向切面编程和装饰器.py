import datetime


# 装饰器
def display_time(func):
    def wrapper(*args):
        t1 = datetime.datetime.now()
        result = func(*args)
        print(result)
        t2 = datetime.datetime.now()
        print(t2 - t1)
        return result

    return wrapper


# 判断是否是偶数
def is_dou(n):
    if n % 2 == 0:
        return n
    else:
        return 0


@display_time
def dou_num(count):
    res = 0
    for i in range(count):
        res += is_dou(i)
    return res


if __name__ == '__main__':
    print(dou_num(10))
