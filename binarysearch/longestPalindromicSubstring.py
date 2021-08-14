class Solution:
    def solve(self, s):

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        LPSLength = 0
        
        for i in range(len(s)):
            for j in range(i, len(s) + 1):

                if s[i:j][::-1] == s[i:j]:
                    length = len(s[i:j])

                    if length > LPSLength:
                        LPSLength = length
        
        return LPSLength 
        