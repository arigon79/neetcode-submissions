# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 , num2 = [], []
        cur1 = l1
        while cur1:
            num1.append(cur1.val)
            cur1 = cur1.next
        cur2 = l2
        while cur2:
            num2.append(cur2.val)
            cur2 = cur2.next
        n, m = len(num1), len(num2)
        if len(num1) < len(num2):
            num1 += [0] * (len(num2) - len(num1))
        else:
            num2 += [0] * (len(num1) - len(num2))

        res = cur = ListNode()
        carry = 0
        L = len(num1)

        for i in range(L):
            summation = num1[i] + num2[i]
            s = num1[i] + num2[i] + carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next
        
        if carry:
            cur.next = ListNode(carry)
        
        return res.next


         