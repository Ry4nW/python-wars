class Solution:
    def solve(self, a, b):

        intA = int(a, 2)
        intB = int(b, 2)

        return bin(intA + intB)[2:]