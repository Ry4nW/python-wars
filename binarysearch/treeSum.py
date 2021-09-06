# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    treeSum = 0

    def solve(self, root):
        def preOrder(root):
            if root:
                self.treeSum += root.val
                preOrder(root.right)
                preOrder(root.left)
            
            return root
        
        preOrder(root)
        return self.treeSum
        