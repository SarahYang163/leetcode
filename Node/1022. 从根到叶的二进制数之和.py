# https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def process(root: Optional[TreeNode], res_tmp: int):
            # if root is None:
            #     return
            if root.left is None and root.right is None:
                print(res_tmp)
                self.res += (res_tmp << 1) + root.val
                return
            # elif root.left is None:
            #     process(root.right,(res_tmp<<1)+root.val)
            # elif root.right is None:
            #     process(root.left,(res_tmp<<1)+root.val)
            # else:
            #     process(root.left,(res_tmp<<1)+root.val)
            #     process(root.right,(res_tmp<<1)+root.val)
            if root.left is not None:
                process(root.left, (res_tmp << 1) + root.val)
            if root.right is not None:
                process(root.right, (res_tmp << 1) + root.val)

        process(root, 0)
        return self.res
