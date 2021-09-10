# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    count = 0
    
    def solve(self, root, lo, hi):
        def preOrder(root, lo, hi):
            if root:
                if root.val <= hi and root.val >= lo:
                    self.count += 1

                preOrder(root.left, lo, hi)
                preOrder(root.right, lo, hi)

            return root
        
        preOrder(root, lo, hi)
        return self.count
