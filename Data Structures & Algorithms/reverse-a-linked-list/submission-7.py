# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        # Time complexity: O(n)
        # Space Complexity: O(1)
        while cur != None:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev