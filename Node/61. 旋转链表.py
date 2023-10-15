# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置
# https://leetcode.cn/problems/rotate-list/
# Definition for singly-linked list.
import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 借助数组解法
        # if head is None:
        #     return head
        # arr = []
        # while head != None:
        #     arr.append(head.val)
        #     head = head.next
        # n = len(arr)
        # k = k % (n)
        # arr = arr[n - k + 1:] + arr[:n - k + 1]
        # print(arr)
        # head = ListNode(arr[0])
        # p = head
        # for i in range(1, n):
        #     head.next = ListNode(arr[i])
        #     head = head
        # return p
        # [1,2,3,4,5,6,7] 5
        # 不借助数组
        cnt = 0
        node = head
        while node != None:
            cnt += 1
            node = node.next
        k = k % cnt
        node = head
        i = cnt - k
        while i != 1:
            i -= 1
            node = node.next
        print(node.val)
        p = node.next
        if p is None:
            return head
        node.next = None
        k = p
        while k.next != None:
            k = k.next
        k.next = head
        return p


if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "c"
    # res = ""
    # min_ = sys.maxsize
    for letter in letters:
        if letter > target:
            print(letter)
    # return res
    print(letters[0])
