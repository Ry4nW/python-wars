class Solution:
    def solve(self, s, shifts):
        s = list(s)
        alph = 'abcdefghijklmnopqrstuvwxyz'

        for i in range(len(shifts)):
            shift = shifts[i]
            for j in range(i + 1):
                s[j] = alph[shift - (shift // 26)]
        
        return ''.join(s)
