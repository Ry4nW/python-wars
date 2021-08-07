#TLEs
class Solution:
    def solve(self, nums):

        largestSum = float('-inf')
        
        for i in range(len(nums)):

            for j in range(i, len(nums) + 1):

                curSum = sum(nums[i:j + 1])
                largestSum = curSum if curSum > largestSum else largestSum
        
        return largestSum 
