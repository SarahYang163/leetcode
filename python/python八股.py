# Python中的 *args 和 **kwargs区别
#都是处理函数可变参数，*args被打包为远足，**kwargs被打包为字典

def print_multiple_args(*args):
    print(type(args), args)
    map_tmp = {}
    map_tmp[0] = 0
    map_tmp[1] = 1
    for idx in enumerate(map_tmp):
        print(idx)


def print_multiple_kwargs(**kwargs):
    print(type(kwargs), kwargs)
    for idx, val in enumerate(kwargs):
        print(idx, val)


if __name__ == '__main__':
    print_multiple_kwargs(**dict(a=1, b=2, c=1))
