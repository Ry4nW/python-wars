# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    inorderSuccessor = float('inf')
    found = False

    def solve(self, root, t):

        def inorderTraversal(root, t): 

            if root:
                inorderTraversal(root.left, t)
                if root.val > t and root.val < self.inorderSuccessor:
                    self.inorderSuccessor = root.val
                    return root
                inorderTraversal(root.right, t)
            
            return root
        
        inorderTraversal(root, t)
        return self.inorderSuccessor
