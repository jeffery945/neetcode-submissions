# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if p is None and q is None:
                return True
            if p is None and q:
                return False
            if q is None and p:
                return False
            if p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            else:
                return False

        return dfs(p, q)