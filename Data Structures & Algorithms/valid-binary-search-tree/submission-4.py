# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(root, float('-inf'), float('inf'))
        
    def validBST(self, node, left, right):
        if not node:
            return True
        
        if left < node.val < right:
            return self.validBST(node.left, left, node.val) and self.validBST(node.right, node.val, right)
        
        return False

        