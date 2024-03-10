# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool: 
        # if there's a NULL node, it must be the last node of the BST.
        if root is None:
            return True
        
        q = deque()
        q.append(root)
        flag = False # Null Node?

        while q:
            curr = q.popleft()
            if not curr: # NULL node?
                flag = True
            else:
                if flag == True:
                    return False
                
                q.append(curr.left)
                q.append(curr.right)
         
        return True
