import random

map_ = {4: 32432, 8745: 649774, 9: 3498749, 54478323: 4, 584: 96699696}
# a = sorted(map_)
# print(a)
# print(map_.items())
# print(map_.keys())
# 按照第一个元素倒叙
# [(54478323, 4), (8745, 649774), (584, 96699696), (9, 3498749), (4, 32432)]
# k = sorted(map_.items(), key=lambda x: (-x[0], x[1]))
# 按照第一个元素正序
# [(4, 32432), (9, 3498749), (584, 96699696), (8745, 649774), (54478323, 4)]
# k = sorted(map_.items(), key=lambda x: (x[0], x[1]))
# 按照第二个元素正序
# [(54478323, 4), (4, 32432), (8745, 649774), (9, 3498749), (584, 96699696)]
# k = sorted(map_.items(), key=lambda x: (x[1], x[0]))
# 按照第二个元素倒叙
# [(584, 96699696), (9, 3498749), (8745, 649774), (4, 32432), (54478323, 4)]
# k = sorted(map_.items(), key=lambda x: (-x[1], x[0]))
# 按照第二个元素正序，第一个元素倒叙
# [(54478323, 4), (4, 32432), (8745, 649774), (9, 649774), (584, 96699696)]
map_ = {4: 32432, 8745: 649774, 9: 649774, 54478323: 4, 584: 96699696}
k = sorted(map_.items(), key=lambda x: (x[1], - x[0]))

print(k)
print(type(k))

# apple = [3, 5, 4, 2, 5, 6, 2, 2, 2, 4, 5, 56, 43, 2, 2, 4, 4]
# print(apple.sort(key=lambda x: x[1]))
#
if __name__ == '__main__':
    #
    #     s = []
    #     for i in range(30):
    #         a = []
    #         a.append(i + 1)
    #         score = random.randint(10, 100)
    #         a.append(score)
    #         s.extend([a])
    #     list = sorted(s, key=lambda x: x[1], reverse=True)  # 降序排序
    #
    #     for i in range(10):  # 输出前十位同学的成绩
    #         print("编号为{:02}的同学成绩是:{:2}分".format(list[i][0], list[i][1]))
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("按值(value)排序:")
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))
