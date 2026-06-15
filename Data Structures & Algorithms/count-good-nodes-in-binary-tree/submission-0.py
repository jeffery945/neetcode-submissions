# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxvalue = 0
        def dfs(node, maxvalue):
            if not node:
                return 0
            
            res = 1 if node.val >= maxvalue else 0
            maxvalue = max(maxvalue, node.val)
            res += dfs(node.left, maxvalue)
            res += dfs(node.right, maxvalue)
            return res

        return dfs(root, root.val)