# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([(0, root)])
        largest_val = defaultdict(lambda: float("-inf"))
        while q:
            level, tree = q.popleft()
            largest_val[level] = max(largest_val[level], tree.val)
            
            if tree.left:
                q.append((level + 1, tree.left))
            if tree.right:
                q.append((level + 1, tree.right))
        
        return list(largest_val.values())
        
"""
1. in binary tree, find the largest value at each level of the tree
2. using queue, bfs
"""