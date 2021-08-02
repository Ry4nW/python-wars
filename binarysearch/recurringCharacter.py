class Solution:
    def solve(self, s):

        characters = []

        for i in range(len(s)):
            if s[i] not in characters:
                characters.append(s[i])
            else:
                return i
        
        return -1
        