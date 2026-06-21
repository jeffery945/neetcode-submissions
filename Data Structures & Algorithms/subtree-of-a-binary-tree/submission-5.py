# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subroot):
            if not root and not subroot:
                return True
            elif not root:
                return False
            elif not subroot:
                return False
            elif root and subroot and root.val == subroot.val:
                return sameTree(root.left, subroot.left) and sameTree(root.right, subroot.right)
            else:
                return False
        if not root:
            return False
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)