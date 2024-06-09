# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        fi, self.se = root.val, float('inf')

        def dfs(node):
            if node:
                if fi < node.val < self.se:
                    self.se = node.val
                elif node.val == fi:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.se if self.se < float('inf') else -1