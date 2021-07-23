class Solution:
    def solve(self, s0, s1):

        if ''.join(sorted(s0)) in ''.join(sorted(s1)) and (len(s0) == len(s1)):
            return True
        
        return False