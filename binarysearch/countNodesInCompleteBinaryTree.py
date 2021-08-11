class Tree:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    nodeCount = 0

    def solve(self, root):

        if root:
            self.nodeCount += 1
            self.solve(root.left)
            self.solve(root.right)
        
        return self.nodeCount
        