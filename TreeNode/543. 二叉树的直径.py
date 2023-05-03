# https://leetcode.cn/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ReturnData:
    def __init__(self, size: int, high: int):
        self.maxSize = size
        self.high = high


class Solution:
    # 利用每个子树的长度
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     self.res = -sys.maxsize - 1
    #
    #     def process(root: Optional[TreeNode]) -> int:
    #         if root is None:
    #             return 0
    #         leftSize = process(root.left)
    #         rightSize = process(root.right)
    #         self.res = max(self.res, leftSize + rightSize)
    #         return max(leftSize, rightSize) + 1
    #
    #     process(root)
    #     return self.res

    # 构造返回函数
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def process(root: Optional[TreeNode]) -> ReturnData:
            if root is None:
                return ReturnData(0, 0)
            leftData = process(root.left)
            rightData = process(root.right)
            rootSize = max(max(leftData.maxSize, rightData.maxSize), leftData.high + rightData.high)
            rootHigh = max(leftData.high, rightData.high) + 1
            return ReturnData(rootSize, rootHigh)

        return process(root).maxSize

    def progress(self, m: int, k: int, p: int, n: int) -> int:
        # m：现在的位置
        # k：目标位置
        # p: 剩余步数
        # res: 方法数
        if p == 0:
            if m == k:
                return 1
            else:
                return 0
        self.res = 0
        if m == 1:
            # 只能向右
            return self.res + self.progress(m + 1, k, p - 1, n)
        if m == n:
            # 只能向左
            return self.res + self.progress(m - 1, k, p - 1, n)
        return self.res + self.progress(m + 1, k, p - 1, n) + self.progress(m - 1, k, p - 1, n)


if __name__ == '__main__':
    res = Solution()
    print(res.progress(2, 3, 3, 4))
