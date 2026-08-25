# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpath = root.val
        def dfs(root):
            nonlocal maxpath

            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)
            maxpath = max(maxpath, root.val + left + right)
            return max(root.val + left, root.val + right)

        dfs(root)
        return maxpath