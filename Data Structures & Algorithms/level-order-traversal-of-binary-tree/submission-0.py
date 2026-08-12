# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        self.helper(root, arr, 0)
        return arr

    def helper(self, root, arr, level):
        if not root:
            return
        if len(arr) - 1 >= level:
            arr[level].append(root.val)
        else:
            arr.insert(level, [root.val])
        print(arr)
        self.helper(root.left, arr, level + 1)
        self.helper(root.right, arr, level + 1)

