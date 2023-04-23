class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inOrderUnrecur(head: Node):
    stack = []
    stack.append(head)
    while len(stack) != 0:
        node = stack.pop()
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
