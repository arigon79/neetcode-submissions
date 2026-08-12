# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First, find the length of the list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # If we need to remove the head
        if n == length:
            return head.next

        # Find the node just before the one to remove
        cur = head
        for _ in range(length - n - 1):
            cur = cur.next

        # Remove the nth node
        cur.next = cur.next.next

        return head