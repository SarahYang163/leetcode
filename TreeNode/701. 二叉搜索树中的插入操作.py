# https://leetcode.cn/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#测试用例
# [4,2,7,1,3]
# 5
# [40,20,60,10,30,50,70]
# 25
# [4,2,7,1,3,null,null,null,null,null,null]
# 5
# [5,null,14,10,77,null,null,null,95,null,null]
# 4
# []
# 5

from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
        if root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        elif root.val > val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        return root
