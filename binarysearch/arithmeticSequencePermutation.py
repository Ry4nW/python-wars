class Solution:
    def solve(self, nums):

        nums.sort() 
        firstSortedDifference = nums[1] - nums[0]

        for i in range(2, len(nums)):

            if nums[i] - nums[i - 1] != firstSortedDifference:
                return False
        
        return True