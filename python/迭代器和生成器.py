# 迭代器
x = [1, 2, 3, 4]
y = iter(x)
next(y)
next(y)
next(y)
# 生成器
# 相比于迭代器的优势是，生成器并不会像迭代器一样占用大量内存。比如声明一个迭代器：[i for i in range(100000000)]就可以声明一个包含一亿个元素的列表，每个元素在生成后都会保存到内存中。但实际上我们也许并不需要保存那么多东西，只希望在你用 next() 函数的时候，才会生成下一个变量，因此生成器应运而生，在python中的写法为(i for i in range(100000000))
a = (1, 2, 3, 4)
b = iter(a)
next(b)
next(b)
next(b)

# 生成器还可以有别的形式，比如生成器函数，通过yield关键字，把结果返回到next()方法中，举个例子：
if __name__ == '__main__':
    def frange(start, stop, increment):
        x = start
        while x < stop:
            yield x
            x += increment


    # for n in frange(0, 2, 0.5):
    #     print(n)
    g = frange(0, 2, 0.5)
    for i in g:
        print(i)
    # print(next(g))
# 相比于迭代器，生成器具有以下优点：
#
# 减少内存
# 延迟计算
# 有效提高代码可读性
