# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        # Time: O(n*logn)
        # Space: O(n)

        def dfs(node):
            if not node:
                return
            
            heapq.heappush(heap, node.val)
            
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)

        return heapq.nsmallest(k, heap)[-1]