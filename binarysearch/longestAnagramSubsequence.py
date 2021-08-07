class Solution:
    def solve(self, a, b):

        count = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for i in alphabet:
            count += min(a.count(i), b.count(i))
        
        return count
        