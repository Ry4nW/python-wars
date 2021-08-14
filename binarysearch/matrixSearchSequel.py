class Solution:
    def solve(self, matrix, target):
        
        for row in matrix:
            if target in row:
                return True
        
        return False
        