class Solution:
    def solve(self, s):

        currentChar = s[0]
        compressedString = ''

        for i in s:
            if i != currentChar:
                compressedString += currentChar
                currentChar = i

        try:
            return compressedString if compressedString[-1] == currentChar else compressedString + currentChar
        except:
            return s[0]
        