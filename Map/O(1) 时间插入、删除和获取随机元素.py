from random import randint


# https://leetcode.cn/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.size = 0
        self.index_map = dict()
        self.map_index = dict()

    def insert(self, val: int) -> bool:
        if val in self.map_index:
            return False
        else:
            self.size += 1
            self.index_map[self.size] = val
            self.map_index[val] = self.size
            return True

    def remove(self, val: int) -> bool:
        if self.size == 0 or val not in self.map_index:
            return False
        elif self.size == 1:
            self.index_map.pop(self.size)
            self.map_index.pop(val)
            self.size -= 1
            return True
        else:
            # 在第二个map找到在val 对应的索引 index
            index = self.map_index[val]
            last_val = self.index_map[self.size]
            # 把最后一个值付给index 在第一个map中
            self.index_map[index] = self.index_map[self.size]
            self.map_index.pop(val)
            self.map_index[last_val] = index
            self.index_map.pop(self.size)
            self.size -= 1
            return True

    def getRandom(self) -> int:
        return self.index_map[randint(1, self.size)]
