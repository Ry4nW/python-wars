class Solution:
    def solve(self, intervals):
        intervals.sort()

        if len(intervals) == 1:
            return intervals[0][1] - intervals[0][0] + 1

        i = 0
        longestInterval = 0

        while i < len(intervals):

            if i < len(intervals) - 1 and intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = max(intervals[i + 1][1], intervals[i][1])
                del intervals[i + 1]
                i -= 1
                        
            dif = intervals[i][1] - intervals[i][0] + 1
            longestInterval = dif if longestInterval < dif else longestInterval
            i += 1

        return longestInterval
        