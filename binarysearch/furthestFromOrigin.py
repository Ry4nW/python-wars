class Solution:
    def solve(self, s):
        
        lCount = 0
        rCount = 0
        choiceCount = 0

        for i in s:
            if i == 'L':
                lCount += 1
            elif i == 'R':
                rCount += 1
            else:
                choiceCount += 1
        
        if lCount > rCount:
            return (lCount + choiceCount) - rCount
        else:
            return (rCount + choiceCount) - lCount
        