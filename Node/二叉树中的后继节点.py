"""
 题目https://cloud.tencent.com/developer/article/1606341
 二叉树中找到一个节点的后继节点，前继节点
  现在有一种新的二叉树节点类型如下：
    该结构比普通二叉树节点结构多了一个指向父节点parent指针。
    假设有一
    棵Node类型的节点组成的二叉树，树中每个节点的parent指针都正确地指向自己的父节点，头节点的parent指向null。
    只给一个在二叉树中的某个节点
    node，分别实现返回node的后继，前继节点的函数。
    在二叉树的中序遍历的序列中，node的下一个节点叫作node的后继节点，node的上一个节点叫做前节点。
"""
from idlelib.tree import TreeNode


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


def houjijiedian(node: TreeNode):
    if node is None:
        return
    if node.right is not None:
        # 找到右节点最左的节点
        node = node.right
        while node.left is not None:
            node = node.left
        return node
    else:
        # 没有右节点，往上找，找到该节点最为谁的最左的节点
        parentNode = node.parent
        while parentNode is not None:
            if node is parentNode.left:
                return node
            else:
                node = parentNode
                parentNode = parentNode.parent
        return
