# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def solve(self, root):
        
        def inorderTraverse(root, inorderTraversal):
            if root:
                inorderTraversal = inorderTraverse(root.left, inorderTraversal)
                inorderTraversal.append(root.val)
                inorderTraversal = inorderTraverse(root.right, inorderTraversal)
            
            return inorderTraversal
        
        return inorderTraverse(root, [])
