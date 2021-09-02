class Solution:
    def solve(self, n):
        
        def isPrime(n):
            
            if n <= 1 :
                return False
        
            for i in range(2, n):
                if n % i == 0:
                    return False
        
            return True

        def printPrime(n):

            primes = []

            for i in range(2, n + 1):
                if isPrime(i):
                    primes.append(i)
            
            return primes
        
        return printPrime(n)
        