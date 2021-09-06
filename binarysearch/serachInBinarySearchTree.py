# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    found = False

    def solve(self, root, val):

        def preOrder(root):

            if root:
                if root.val == val:
                    self.found = True
                    return root
                preOrder(root.right)
                preOrder(root.left)
            
            return root
        
        preOrder(root)
        return self.found
        