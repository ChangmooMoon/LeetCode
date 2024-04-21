# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_height(node):
            h = 0
            while node.left:
                node = node.left
                h += 1
            return h

        def check_right(i, h, node) -> bool:
            l, r = 0, 2**h - 1
            for _ in range(h):
                mid = (l + r) // 2
                if i <= mid:
                    node = node.left
                    r = mid
                else:
                    node = node.right
                    l = mid + 1
            return node is not None

        h = get_height(root)
        if h == 0:
            return 1
        
        l, r = 1, 2**h - 1 # left, right max count
        while l <= r:
            mid = (l + r) // 2
            if check_right(mid, h, root): # is right node exist?
                l = mid + 1
            else:
                r = mid - 1
        
        return 2**h - 1 + l