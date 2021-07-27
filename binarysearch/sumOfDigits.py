class Solution:
    def solve(self, n):

        s = 0

        while n:
            s += n % 10
            n //= 10
            
        return s
