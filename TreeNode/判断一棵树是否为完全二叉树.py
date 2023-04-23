class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 完全二叉树定义：完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大，第 n 层有 2n-1 个节点）的，并且所有的节点都尽可能地集中在左侧
#java实现
    # public class TreeNode {
    #     int val;
    #     TreeNode left;
    #     TreeNode right;
    #
    #     TreeNode() {
    #     }
    #
    #     TreeNode(int val) {
    #         this.val = val;
    #     }
    #
    #     TreeNode(int val, TreeNode left, TreeNode right) {
    #         this.val = val;
    #         this.left = left;
    #         this.right = right;
    #     }
    # }
    #
    # public boolean isCompleteTree (TreeNode head) {
    #     // write code here
    #     Queue<TreeNode> queue = new LinkedList<>();
    #     boolean leaf = false;
    #     queue.add(head);
    #     while (queue.size() != 0) {
    #         TreeNode node = queue.poll();
    #         TreeNode l = node.left;
    #         TreeNode r = node.right;
    #         if ((leaf && (l != null || r != null)) || (r != null) && (l == null)) {
    #             return false;
    #         }
    #         if ((r == null) || (l == null)) {
    #             leaf = true;
    #         }
    #         if (l != null) {
    #             queue.add(l);
    #         }
    #         if (r != null) {
    #             queue.add(r);
    #         }
    #     }
    #     return true;
    # }