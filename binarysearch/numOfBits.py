class Solution:
    def solve(self, n):

        bitCount = 0
        intInBinary = bin(n)

        for i in range(2, len(intInBinary)):
            if intInBinary[i] == '1':
                bitCount += 1

        return bitCount
