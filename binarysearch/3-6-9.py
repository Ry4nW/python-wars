class Solution:
    def solve(self, n):

        threeSixNine = []

        for i in range(1, n + 1):

            if i % 3 == 0 or ('3' in str(i) or '6' in str(i) or '9' in str(i)):
                threeSixNine.append('clap')
            else:
                threeSixNine.append(str(i))
        
        return threeSixNine