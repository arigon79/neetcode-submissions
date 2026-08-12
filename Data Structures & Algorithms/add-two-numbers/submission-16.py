# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # [1,2,3], l2 = [4,5, 0]
        carry = 0
        cur1, cur2 = l1, l2
        dummy = ListNode()
        cur = dummy
        
        while cur1 and cur2:
            s = cur1.val + cur2.val + carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur1 = cur1.next
            cur2 = cur2.next
            cur = cur.next
        
        while cur1:
            s = cur1.val + carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur1 = cur1.next
            cur = cur.next
        while cur2:
            s = cur2.val + carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur2 = cur2.next
            cur = cur.next
        
        if carry:
            cur.next = ListNode(carry)
        
        return dummy.next
            


            

        
