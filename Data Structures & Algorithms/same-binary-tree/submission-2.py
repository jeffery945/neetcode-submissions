# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None and root2:
                return False
            elif root2 is None and root1:
                return False
            elif root1.val == root2.val:
                return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
            else:
                return False
        return dfs(p, q)