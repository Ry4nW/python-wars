# Attempt

class Solution:
    def solve(self, s):

        palindromeCount = 0

        for i in range(len(s)):

            for j in range(len(s[i:])):

                if s[i:j + i + 1] == s[i:j + i + 1][::-1]:

                    palindromeCount += 1
        
        return palindromeCount