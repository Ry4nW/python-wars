# TO DEBUG

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prevLevel = None
    def solve(self, root):
        def dfs(node, visited=set(), level=0):
            if node and node not in visited:
                visited.add(node)
                if not node.left and not node.right:
                    if self.prevLevel and level != self.prevLevel:
                        self.prevLevel = None
                        return False
                    self.prevLevel = level
                dfs(node.left, visited, level + 1)
                dfs(node.right, visited, level + 1)
            
        dfs(root)
        if self.prevLevel: return True
        return False
