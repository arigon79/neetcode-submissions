# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float("inf")

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            left_val = dfs(root.left)
            left_val = max(left_val, 0)
            
            right_val = dfs(root.right)
            right_val = max(right_val, 0)
            res = max(res, root.val + left_val + right_val)
            
            return root.val + max(left_val, right_val)

        dfs(root)
        return res
            

