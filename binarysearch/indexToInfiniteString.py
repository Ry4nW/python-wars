class Solution:
    def solve(self, s, i, j):

        chars = []

        for i in range(i, j):

            chars.append(s[i % len(s)])
        
        return ''.join(chars)
        