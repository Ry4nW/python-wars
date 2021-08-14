class Solution:
    def solve(self, s):

        decodedString = ''
        numLength = ''

        for i in s:

            if i.isdigit():
                numLength += i
            else:
                decodedString += i * int(numLength)
                numLength = ''
        
        return decodedString
