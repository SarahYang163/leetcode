# https://leetcode.cn/problems/binary-tree-level-order-traversal/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        store_node_every_layer = []
        res_total = []
        res_total.append(root.val)
        store_node_every_layer.append(root)
        while len(store_node_every_layer) != 0:
            res_layer = []
            res_layer_value = []
            for node in store_node_every_layer:
                if node.left is not None:
                    res_layer.append(node.left)
                    res_layer_value.append(node.left.val)
                if node.right is not None:
                    res_layer.append(node.right)
                    res_layer_value.append(node.right.val)

            if len(res_layer) != 0:
                res_total.append(res_layer)
            else:
                break
            store_node_every_layer = res_layer
        return res_total.reverse()
