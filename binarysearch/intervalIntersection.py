class Solution:
    def solve(self, intervals):
        
        maxStart = intervals[0][0]
        maxEnd = intervals[0][1]

        for i in range(1, len(intervals)):

            if intervals[i][0] > maxStart:
                maxStart = intervals[i][0]
            
            if intervals[i][1] < maxEnd:
                maxEnd = intervals[i][1]
        
        return [maxStart, maxEnd]
        