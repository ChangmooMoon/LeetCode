# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):
    def __init__(self, root):
        self.nums = set()
        q = [[root, 0]]
        while q:
            tree, num = q.pop(0)
            tree.val = num
            self.nums.add(num)
            
            if tree.left:
                q.append([tree.left, 2 * num + 1])
            if tree.right:
                q.append([tree.right, 2 * num + 2])
        """
        :type root: TreeNode
        """
    def find(self, target):
        return target in self.nums
        """
        :type target: int
        :rtype: bool
        """
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)