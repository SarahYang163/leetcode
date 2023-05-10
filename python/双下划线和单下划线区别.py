class foo:
    def __init__(self):
        self.name = "test"
        self.age = 12

    # 双下划线开头的方法就是类里面的私有方法
    def __method(self):
        print("__method")
        print(self.name)
        print(self.age)

    def method(self):
        print("method")
        print(self.name)
        print(self.age)


class foo2(foo):
    def __init__(self):
        super().__init__()
        # super().method()
        self._foo__method()


class demo():
    def __init__(self):
        self.name = "test"
        self.age = 12

    def _method(self):
        print(self.name)
        print(self.age)


if __name__ == '__main__':
    # demo = foo()
    # demo.method()
    # demo._foo__method()

    # demo2 = foo2()
    d = demo()
    d._method()
