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


if __name__ == '__main__':
    print(transportationHub([[0, 1], [0, 3], [1, 3], [2, 0], [2, 3]]))
