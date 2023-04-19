from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 完全二叉树定义：完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大，第 n 层有 2n-1 个节点）的，并且所有的节点都尽可能地集中在左侧
# leetcode link:https://leetcode.cn/problems/count-complete-tree-nodes/
class Solution:
    res = 0

    # def countNodes(self, root: Optional[TreeNode]) -> int:
    #     return self.process(root)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        h = self.Treehigh(root)
        print(f'h:', h)
        h_right = self.Treehigh(root.right)
        self.res += 2 ** h_right

        if h_right is h - 1:
            self.countNodes(root.right)
        else:
            self.countNodes(root.left)
        return self.res

    def Treehigh(self, head: TreeNode) -> int:
        if head is None:
            return 0
        return max(self.Treehigh(head.left), self.Treehigh(head.right)) + 1
