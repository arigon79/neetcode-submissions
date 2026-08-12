# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time complexity: O(n)
        # Space complexity: O(1)
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l += 1
        cnt = 0
        cur, prev = head, None

        if l - n == 0:
            temp = cur.next
            cur = None
            head = temp
            return head   

        while cur:
            prev = cur
            cur = cur.next
            cnt += 1
            if cnt == l - n:
                prev.next = cur.next
                cur = None

        return head
            


        
        