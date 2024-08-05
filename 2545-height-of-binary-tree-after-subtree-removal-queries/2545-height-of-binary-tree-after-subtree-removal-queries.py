# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def get_height(node):
            if not node:
                return 0
            l, r = get_height(node.left), get_height(node.right)
            h_dict[node] = max(l, r) + 1
            return h_dict[node]
            

        def dfs(node, depth, etc):
            if not node:
                return
            when_target_removed[node.val] = etc
            dfs(node.left, depth + 1, max(etc, depth + 1 + h_dict[node.right]))
            dfs(node.right, depth + 1, max(etc, depth + 1 + h_dict[node.left]))


        h_dict = defaultdict(int)
        get_height(root)
        when_target_removed = [0] * (len(h_dict) + 1)
        dfs(root, -1, 0)

        ans = []
        for q in queries:
            ans.append(when_target_removed[q])
        
        return ans
