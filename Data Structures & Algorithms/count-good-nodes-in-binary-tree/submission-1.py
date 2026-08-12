# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # time complexity: O(n)
        # space complexity: O(n)
        count = 0
        
        def dfs(node, val):
            nonlocal count

            if not node:
                return
            
            if node.val >= val:
                count += 1
            
            dfs(node.left, max(val, node.val))
            dfs(node.right, max(val, node.val))
            return 
        
        dfs(root, root.val)
        return count

