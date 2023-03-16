# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ans = ""
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = str(root.val)
        
        if root.left:
            ans += '(' + self.tree2str(root.left) + ')'
            
        if root.right:
            if not root.left:
                ans += '()'
            ans += '(' + self.tree2str(root.right) + ')'
            
        return ans
        
'''
1. 프리오더 루왼오 순으로 방문
그려진 트리가 주어졌으니까, 이걸 가지고 preorder 방문을 하면서 string을 만든다

'''