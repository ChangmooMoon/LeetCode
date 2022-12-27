# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, t1, t2) -> bool:
        if t1 and t2: # mid, left, right 비교
            return t1.val == t2.val and self.isSame(t1.left, t2.left) and self.isSame(t1.right, t2.right)
        return t1 is t2
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        