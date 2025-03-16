# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        while q:
            node, dep = q.popleft()
            if not node.left and not node.right:
                return dep
            
            for next_node in [node.left, node.right]:
                if next_node:
                    q.append((next_node, dep+1))
            