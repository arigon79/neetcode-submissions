# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # Time: O(n)
        # Space: O(n)
        def dfs(root, i):
            nonlocal res

            if not root:
                return
            
            if len(res) > i:
                res[i].append(root.val)
            else:
                res.append([root.val])
            print(res, i)
            dfs(root.left, i + 1)
            dfs(root.right, i + 1)
            return
        
        dfs(root, 0)
        return res
            