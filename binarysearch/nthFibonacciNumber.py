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
        