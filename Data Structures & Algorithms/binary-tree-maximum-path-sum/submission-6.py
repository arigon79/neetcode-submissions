# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(root):
            nonlocal res

            if not root:
                return 0

            left_val = max(0, dfs(root.left))
            right_val = max(0, dfs(root.right))

            res = max(res, left_val + right_val + root.val)
            return root.val + max(left_val, right_val)
        
        dfs(root)
        return res