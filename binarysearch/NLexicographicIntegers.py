class Solution:
    def solve(self, n):

        stringElements = [str(num) for num in range(1, n + 1)]
        stringElements.sort()
        return [int(num) for num in stringElements]
        