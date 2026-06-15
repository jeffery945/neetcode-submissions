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
        def dfs(root, level):
            if not root:
                return None
            
            while len(res) <= level:
                res.append([])
            res[level].append(root.val)
            level += 1
            dfs(root.left, level)
            dfs(root.right, level)
        dfs(root, level)
        return res