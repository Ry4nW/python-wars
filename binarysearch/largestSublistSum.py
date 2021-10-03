class Solution:
    def solve(self, nums):

        ans, maxSum, minSum = nums[0], 0, 0

        for i in range(len(nums)):
            maxSum += nums[i]
            ans = max(ans, maxSum - minSum)
            minSum = min(minSum, maxSum)
        
        return ans

solution = Solution()
print(solution.solve([10, -5, 12, -100, 3, -1, 20]))
