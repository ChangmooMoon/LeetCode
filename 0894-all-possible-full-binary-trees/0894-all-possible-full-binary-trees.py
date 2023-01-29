# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        elif n == 1:
            return [TreeNode(0)]
        
        else:  
            ans = []
            for left_n in range(n):
                right_n = n - 1 - left_n

                for i in self.allPossibleFBT(left_n):
                    for j in self.allPossibleFBT(right_n):
                        tree = TreeNode(0)
                        tree.left = i
                        tree.right = j
                        ans.append(tree)
            return ans
            
        
        
            
            
        
'''
1. 노드 n개로 만들수있는 모든 완전이진트리 모양 리턴하기
n 1~20
'''