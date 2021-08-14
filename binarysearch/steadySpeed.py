class Solution:
    def solve(self, positions):

        longestCount = 0
        curCount = 1
        prevChange = None

        for i in range(1, len(positions)):
            curChange = abs(positions[i] - positions[i - 1])
            
            if curChange != prevChange:
                prevChange = curChange
                longestCount = longestCount if curCount < longestCount else curCount
                curCount = 2
                continue
            
            curCount += 1
        
        return longestCount if curCount < longestCount else curCount
        