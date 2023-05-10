# __new__主要用在单例模式的情景下
class book:
    # __new__是在实例创建之前调用的，因为他的任务就是创建实例然后返回该实例，是一个静态方法
    def __new__(self, title):
        print("__new__")
        return super().__new__(self)

    # __init__是当实例对象创建完成之后被调用的，然后设置对象属性的一些初始值
    def __init__(self, title):
        print("__init__")
        super().__init__()
        self.title = title
    # 也就是说new方法在init方法之前被调用，new的返回值是实例
    # 将传递给init方法的第一个参数，然后init给这个实例设置一些参数


# 单例模式
# 一个类实例化出来的对象都是同一个
class palyer:
    __instance = None
    __flag = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        print("in new")
        return cls.__instance

    def __init__(self):
        if not self.__flag:
            print("in init")
            self.__flag = True


# 还有两种写法
# 装饰器

def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Foo:
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)  # True


# 使用元组
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=Singleton):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)  # True

if __name__ == '__main__':
    video = palyer()
    music = palyer()
