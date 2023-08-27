# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        global ans
        ans = []
        self.dfs(root, 0)
        return ans

    def dfs(self, node, depth):
        if not node:
            return
        
        if len(ans) == depth:
            ans.append(node.val)

        self.dfs(node.right, depth + 1) # 오른쪽부터
        self.dfs(node.left, depth + 1)

"""
1. root + right side node return, array tree
2, node 100개, implement tree, retrieve right side
오른쪽에서 봤을 때 보이는 노드, right가 없으면 left가 보임
arr로 표현해서 오른쪽 노드가 있으면 오른쪽 추가, 없으면 왼쪽 노드 추가, 둘다 없으면 종료
"""