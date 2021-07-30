class Solution:
    def solve(self, n):
        
        for i in str(n):

            if i != '3':
                return int(str(n).replace(i, '3', 1))
        
        return n