class Solution:
    def solve(self, s):
        count = 0
        res = 0

        for i in s:
            if i == '1':
                count += 1
            else:
                count = 0
            res += count
        
        return res % (10 ** 9 + 7)
        