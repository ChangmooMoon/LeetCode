# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        return self.cnt if self.dfs(root) else self.cnt+1

    def dfs(self, node: TreeNode):
        if node == None:
            return 1
        left, right = self.dfs(node.left), self.dfs(node.right)
        if left == 0 or right == 0:
            self.cnt += 1
            return 2
        elif left == 2 or right == 2:
            return 1
        else:
            return 0