class Solution:
    def solve(self, n):

        sumAdd = sum(int(i) for i in str(n))

        while sumAdd >= 10:
            sumAdd = sum(int(i) for i in str(sumAdd))
        
        return sumAdd
        
solution = Solution()
print(solution.solve(8835))
        