# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        def bfs(tree):
            q = deque([root])
            res = []

            while q:
                lv = []
                N = len(q)
                for i in range(N):
                    curr = q.popleft()
                    lv.append(curr.val)
                    
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)

                res.append(lv)
            return res

        return bfs(root)