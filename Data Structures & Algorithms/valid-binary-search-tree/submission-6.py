# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n)
        # Space: O(n)
        return self.isValid(root, -float('inf'), float('inf'))
        
    def isValid(self, node, left, right):
        if not node:
            return True
        if left < node.val < right:
            return self.isValid(node.left, left, node.val) and self.isValid(node.right, node.val, right)
        return False