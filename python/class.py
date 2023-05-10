from 双下划线和单下划线区别 import demo


class soluction:
    num = 1

    # @property
    def test(self):
        print(self.num)


def clear_list(l):
    l = []


def fl(l=[1]):
    l.append(1)
    print(l)


if __name__ == '__main__':
    # ll = [1, 2, 3]
    # clear_list(ll)
    # print(ll)
    # fl()
    # fl()
    # print()
    d = demo()
    d.method()

