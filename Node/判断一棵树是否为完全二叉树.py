class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 完全二叉树定义：完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大，第 n 层有 2n-1 个节点）的，并且所有的节点都尽可能地集中在左侧
#java实现
    # public class Node {
    #     int val;
    #     Node left;
    #     Node right;
    #
    #     Node() {
    #     }
    #
    #     Node(int val) {
    #         this.val = val;
    #     }
    #
    #     Node(int val, Node left, Node right) {
    #         this.val = val;
    #         this.left = left;
    #         this.right = right;
    #     }
    # }
    #
    # public boolean isCompleteTree (Node head) {
    #     // write code here
    #     Queue<Node> queue = new LinkedList<>();
    #     boolean leaf = false;
    #     queue.add(head);
    #     while (queue.size() != 0) {
    #         Node node = queue.poll();
    #         Node l = node.left;
    #         Node r = node.right;
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