import sys


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 搜索二叉树定义：任何节点，左子树<当前节点<右子树

# 修改自中序遍历非递归版本
def sbt(head: Node) -> bool:
    stack = []
    lastNodeVal = -sys.maxsize - 1
    if head is not None:
        while head is not None or len(stack) != 0:
            if head is not None:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                if head.val > lastNodeVal:
                    lastNodeVal = head.val
                else:
                    return False
                head = head.right
    return True
