# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def in_order_traverse(root):
            if root is None:
                return []
            return (in_order_traverse(root.left) + [str(root.val)] + in_order_traverse(root.right))

        traversal = in_order_traverse(root)
        traversalString = ''.join(traversal)    
        return traversalString == traversalString[::-1]
