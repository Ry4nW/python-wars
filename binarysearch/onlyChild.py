# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    c = 0
    def solve(self, root):
        def traverse(root):
            if root:
                if not (root.left and root.right) and (root.left or root.right):
                    self.c += 1
                traverse(root.left)
                traverse(root.right)

        traverse(root)
        return self.c
