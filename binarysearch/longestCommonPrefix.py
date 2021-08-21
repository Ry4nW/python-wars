class Solution:
    def solve(self, words):

        minimum = sorted(words, key = len)[0]
        LCP = ''

        for i in range(len(minimum)):

            matches = True
            curChar = minimum[i]

            for j in range(len(words)):
                if words[j][i] != curChar:
                    matches = False
                    break

            if not matches:
                return LCP
            
            LCP += curChar
        
        return LCP
