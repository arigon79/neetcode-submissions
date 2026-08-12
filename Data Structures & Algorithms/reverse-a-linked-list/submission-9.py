# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head -> 0 -> 1 -> 2 -> 3 -> Null
        #  Null <-0 <- 1 <- 2 <- 3 <- head
        # Time: O(n)
        # Space: O(1)
        cur = head
        nextP = None
        
        while cur:
            tmp = cur.next
            cur.next = nextP
            nextP = cur
            cur = tmp
        return nextP