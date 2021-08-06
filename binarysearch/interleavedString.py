class Solution:
    def solve(self, s0, s1):

        if len(s1) == 0:
            return s0
        elif len(s0) == 0:
            return s1

        interleavedString = ''

        for i in range(len(s0)):

            interleavedString += s0[0]
            s0 = s0.replace(s0[0], '', 1)

            try:
                interleavedString += s1[0]
            except: 
                break

            s1 = s1.replace(s1[0], '', 1)
    
        return interleavedString + s0 if len(s1) == 0 else interleavedString + s0 + s1
          