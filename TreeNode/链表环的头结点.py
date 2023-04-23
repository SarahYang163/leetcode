# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:  # 有环的情况下fast肯定不为空
            fast = fast.next.next
            slow = slow.next
            if fast is slow:  # 有环的情况下fast一定可以追上slow
                while slow is not head:
                    head = head.next
                    slow = slow.next
                return slow
        return None
