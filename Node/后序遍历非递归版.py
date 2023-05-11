class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 先用一个栈实现中右左，然后输出，就是左右中，即后续遍历
def posOrderUnrecur(head: Node):
    stack1, stack2 = [], []
    stack1.append(head)
    while len(stack1) != 0:
        node = stack1.pop()
        stack2.append(node.val)
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)
    while len(stack2) != 0:
        print(stack2.pop())
