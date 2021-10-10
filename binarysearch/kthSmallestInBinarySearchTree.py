# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, k):
        traversal = []
        def traverse(root):
            if len(traversal) <= k and root:
                traverse(root.left)
                traversal.append(root.val)
                traverse(root.right)
            return root
        traverse(root)
        return traversal[k]
