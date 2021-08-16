class Solution:
    def solve(self, matrix, k):

        noDuplicates = []
        
        for row in matrix:
            for i in row:
                noDuplicates.append(i)

        return sorted(noDuplicates)[k]
        