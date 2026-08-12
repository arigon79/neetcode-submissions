# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []

        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        while left <= right:
            arr[left - 1], arr[right - 1] = arr[right - 1], arr[left - 1]
            left += 1
            right -= 1
        
        cur = head
        i = 0
        while cur:
            cur.val = arr[i]
            cur = cur.next
            i += 1
        
        return head
        