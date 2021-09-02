class Solution:
    def solve(self, nums):

        directionChanges = 0

        for i in range(2, len(nums)):

            if nums[i] - nums[i - 1] < 0 and nums[i - 1] - nums[i - 2] > 0:
                directionChanges += 1
            elif nums[i] - nums[i - 1] > 0 and nums[i - 1] - nums[i - 2] < 0:
                directionChanges += 1
        
        return directionChanges
