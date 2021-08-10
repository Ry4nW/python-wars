class Solution:
    def solve(self, nums, k):

        nums.sort()
        i = 0
        minSum = float('inf')

        while i + k <= len(nums):

            curSum = nums[i + k - 1] - nums[i]

            if curSum < minSum:
                minSum = curSum

            i += 1
        
        return minSum
        