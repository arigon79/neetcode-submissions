# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = None

        def findKSmallest(node, k):
            nonlocal count, res

            if not node:
                return None

            findKSmallest(node.left, k)
            count += 1
            
            if count == k:
                res = node.val
                return
            
            findKSmallest(node.right, k)
            return
        
        findKSmallest(root, k)
        return res
            



            



            