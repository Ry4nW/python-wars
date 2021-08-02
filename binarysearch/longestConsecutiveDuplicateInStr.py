class Solution:
    def solve(self, s):

        consecutiveCount = 0
        curCount = 0

        for i in range(len(s)):

            try:
                if s[i + 1] == s[i]:

                    curCount += 1
            
                else:
                    curCount += 1

                    if curCount > consecutiveCount:
                        consecutiveCount = curCount
                
                    curCount = 0
            except:
                if s[i - 1] == s[i]:
                    curCount += 1

        if curCount > consecutiveCount:
            consecutiveCount = curCount 
            
        return consecutiveCount if consecutiveCount != 0 else len(s)
        