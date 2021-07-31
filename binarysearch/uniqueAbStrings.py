class Solution:
    def solve(self, s):

        aCount = 0

        for i in s:

            if i == 'a':
                aCount += 1

        return 2 ** aCount
