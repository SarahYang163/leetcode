from typing import Optional

# https://leetcode.cn/problems/reverse-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        p=None
        while head is not None:
            nextNode=head.next
            head.next=p
            p=head
            head=nextNode
        return p
