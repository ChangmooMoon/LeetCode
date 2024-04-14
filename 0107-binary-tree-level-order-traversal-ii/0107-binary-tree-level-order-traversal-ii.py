# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ret = []
        q = deque([(0, root)]) # lv, curr
        while q:
            lv, curr = q.popleft()
            if len(ret) == lv:
                ret.append([])

            ret[lv].append(curr.val)

            if curr.left:
                q.append((lv + 1, curr.left))
            if curr.right:
                q.append((lv + 1, curr.right))
        
        return ret[::-1]
