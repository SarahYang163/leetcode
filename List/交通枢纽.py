from typing import Counter, List


def transportationHub(path: List[List[int]]) -> int:
    node = set()
    in_map = dict()  # 入站
    out_map = dict()  # 出站
    for x, y in path:
        node.add(x)
        node.add(y)
        in_map[y] = in_map.setdefault(y, 0) + 1
        out_map[x] = out_map.setdefault(x, 0) + 1
    for n in node:
        if in_map.get(n, 0) == len(node) - 1 and out_map.get(n, 0) == 0:
            return n
    return -1


def transportationHub1(path: List[List[int]]) -> int:
    map_ = {}
    for p in path:
        if p[0] not in map_:
            map_[p[0]] = [1, 0]
        else:
            map_[p[0]][0] += 1
        if p[1] not in map_:
            map_[p[1]] = [0, 1]
        else:
            map_[p[1]][1] += 1
    for m in map_.items():
        if m[1][0] == 0 and m[1][1] == len(map_) - 1:
            return m[0]
    return -1


if __name__ == '__main__':
    m = {1: 1}
    print(transportationHub1([[0, 3], [1, 3], [2, 0], [2, 3]]))
