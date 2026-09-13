# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(level, root):
            if not root:
                return None

            if len(res) <= level:
                res.append(root.val)

            dfs(level + 1, root.right)
            dfs(level + 1, root.left)

        dfs(0, root)
        return res