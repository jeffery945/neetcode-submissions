# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxvalue):
            if not root:
                return 0

            res = 1 if root.val >= maxvalue else 0 # count that if this node is good

            maxvalue = max(maxvalue, root.val)
            res += dfs(root.left, maxvalue)
            res += dfs(root.right, maxvalue)

            return res

        return dfs(root, root.val)