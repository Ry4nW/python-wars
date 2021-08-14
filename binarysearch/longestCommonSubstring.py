class Solution:
    def solve(self, s0, s1):

        LCS = 0

        if len(s0) > len(s1):
            length = len(s1)
            string = s0
            sliceStr = s1
        else:
            length = len(s0)
            string = s1
            sliceStr = s0
        
        for i in range(length):
            for j in range(i, length + 1):

                seggment = sliceStr[i:j]

                if seggment in string:
                    LCS = LCS if len(seggment) < LCS else len(seggment)
        
        return LCS
