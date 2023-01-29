# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0 or root.val == 1:
            return root.val
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
            
        
'''
1. 완전이진트리가 주어짐
리프노드는 0 or 1을 가짐
non리프노드는 2 or, 3 and 를 가짐

evaluation 
- 리프노드면 True, false
- 아니면 두개의 child를 or 2나 and 3연산함
노드 1000개

2. recursive하게 연산하는 재귀식을 짜자
'''