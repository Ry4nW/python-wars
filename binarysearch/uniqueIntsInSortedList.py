class Solution:
    def solve(self, nums):

        currentInt = nums[0]
        uniqueIntCount = 1

        for i in nums:

            if i != currentInt:
                currentInt = i
                uniqueIntCount += 1
        
        return uniqueIntCount
        