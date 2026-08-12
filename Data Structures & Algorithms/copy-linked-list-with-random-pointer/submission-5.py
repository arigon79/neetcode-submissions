"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        mapper = {}
        cur, dummy = head, Node(0)
        dumCur = dummy
        while cur:
            dumCur.next = Node(cur.val)
            dumCur = dumCur.next
            mapper[cur] = dumCur
            cur = cur.next
        cur, dumCur = head, dummy.next
        while dumCur and cur:
            dumCur.random = mapper[cur.random] if cur.random else None
            dumCur = dumCur.next
            cur = cur.next
        
        return dummy.next

