# 都可以通过Class.method()的方式使用
# classmethod第一个参数是cls，可以引用类变量
# staticmethod使用起来和普通函数一样，只不过放在类里去组织
# classmethod是为了使用类变量，staticmethod是代码组织的需要，完全可以放到类之外
class Person:
    Country = 'china'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    @classmethod
    def print_country(cls):
        print(cls.Country)

    @staticmethod
    def join_name(first_name, last_name):
        return print(last_name + first_name)


a = Person("china", "Bruce")
a.print_country()
a.print_name()
a.join_name("Bruce", "Lee")
Person.print_country()
Person.print_name(a)
Person.join_name("Bruce", "Lee")
