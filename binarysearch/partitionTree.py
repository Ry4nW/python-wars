from collections import deque

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root:
            return [0, 0]
        
        count = [0, 0]
        queue = deque([])
        queue.append(root)

        traversal = []
        while len(queue) > 0:

            traversal.append(int(queue[0].val))
            root = queue.popleft()

            if not root.left and not root.right:
                count[0] += 1
            else:
                count[1] += 1
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        
        return count
