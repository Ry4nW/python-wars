class Solution:

    # Discover largest prime factor
    def solve(self, n):

        if n == 0:
            return False

        i = 2

        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i

        return n <= 5

    # or just check if there are remaining factors to be discovered:
    def solve(self, n):

        while n % 2 == 0 and n > 0:
            n //= 2
        while n % 3 == 0 and n > 0:
            n //= 3
        while n % 5 == 0 and n > 0:
            n //= 5

        return n == 1

    
        
    