class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class resStructure:
    def __init__(self, balance: bool, high: int):
        self.isBalance = balance
        self.h = high


# 平衡二叉树定义：任何节点，左子树和右子树高度差不超过1


def isBalance(head: Node) -> resStructure:
    res1 = isBalance(head.left)
    if res1.isBalance is False:
        return resStructure[False, 0]
    res2 = isBalance(head.right)
    if res2.isBalance is False:
        return resStructure[False, 0]
    if abs(res1.h - res2.h) > 1:
        return resStructure[False, max(res1.h, 0)]
    else:
        return resStructure[True, max(res1.h, res2.h) + 1]
