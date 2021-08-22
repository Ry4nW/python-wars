from functools import lru_cache

class Solution:
    def solve(self, n):

        # Iterative approach, O(n) time.

        if n <= 1:
            return n
        
        previousFib = 0 
        currentFib = 1

        for i in range(n - 1):

            newFib = previousFib + currentFib
            previousFib = currentFib
            currentFib = newFib
        
        return currentFib
    
    lru_cache(None)
    def solve2(self, n):

        if n <= 2:
            return 1
        return self.solve(n - 1) + self.solve(n - 2)
        