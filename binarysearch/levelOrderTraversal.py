# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root:
            return None
        
        queue = []
        queue.append(root)

        traversal = []
        while len(queue) > 0:

            traversal.append(int(str(queue[0].val)))
            root = queue.pop(0)

            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        
        return traversal
