class Solution:
    def solve(self, s):
        
        answer = 0

        for i in map(int, s):
            answer = 3 * answer + i
        
        return answer