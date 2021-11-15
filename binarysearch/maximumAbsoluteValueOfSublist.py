class Solution:
    def solve(self, nums):
        if not nums:
            return 0
        
        curSum = 0
        maxSum = 0
        positive = nums[0] > 0
        for i in range(1, len(nums)):
            if (positive and nums[i] < 0) or (not positive and nums[i] > 0):
                if abs(curSum) > maxSum: maxSum = abs(curSum)
                curSum = 0
                positive = False
            curSum += nums[i]
        
        return maxSum
