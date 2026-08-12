# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        carry = 0
        c1, c2 = l1, l2
        while c1 and c2:
            v1 = c1.val
            v2 = c2.val
            s = v1 + v2 + carry
            if s >= 10:
                res.append(s % 10)
                carry = s // 10
            else:
                res.append(s)
                carry = 0
            c1 = c1.next
            c2 = c2.next
        while c1:
            v1 = c1.val
            s = v1 + carry
            if s >= 10:
                res.append(s % 10)
                carry = s // 10
            else:
                res.append(s)
                carry = 0
            c1 = c1.next
        while c2:
            v2 = c2.val
            s = v2 + carry
            if s >= 10:
                res.append(s % 10)
                carry = s // 10
            else:
                res.append(s)
                carry = 0
            c2 = c2.next
        print(carry)
        if carry:
            res.append(carry)
        print(res)
        dummy = cur = ListNode()
        i = 0
        while i < len(res):
            cur.next = ListNode(res[i])
            cur = cur.next
            i += 1
        
        return dummy.next

