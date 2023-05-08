# https://leetcode.cn/problems/convert-bst-to-greater-tree/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    sumN=0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        self.convertBST(root.right)
        root.val =self.sumN+root.val
        self.sumN=root.val
        self.convertBST(root.left)
        return root