class Solution:
    def solve(self, n):

        # Manual approach to converting a decimal integer to binary.

        binaryStringOfN = bin(n)

        consecutiveOneCount = 0
        current = 0
    
        for i in range(2, len(binaryStringOfN)):

            if int(binaryStringOfN[i]) != 1:
                consecutiveOneCount = consecutiveOneCount if current <= consecutiveOneCount else current
                current = 0
            else:
                current += 1

        return consecutiveOneCount if consecutiveOneCount >= current else current

