class Solution:
    def solve(self, n):

        if n == 0:
            return '0'

        remainders = []

        while n:
            n, r = divmod(n, 3)
            remainders.append(str(r))
        
        return ''.join(reversed(remainders)) 
        