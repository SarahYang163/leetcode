class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思路：
# 当前节点为空，出栈，找右节点
# 当前节点不为空，压栈，找左节点
def interOrderUnrecur(head: Node):
    stack = []
    while head is not None or len(stack) != 0:
        if head is not None:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            print(head.val)
            head = head.right
