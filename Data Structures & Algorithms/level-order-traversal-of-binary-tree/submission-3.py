# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        res = []
        def dfs(level, root):
            if not root:
                return None

            if len(res) <= level:
                res.append([])
            res[level].append(root.val)
            dfs(level + 1, root.left)
            dfs(level + 1, root.right)
        dfs(level, root)
        return res