class Solution:
    def solve(self, nums):

        ascendingNums = sorted(nums)
        descendingNums = sorted(nums, reverse = True)

        ascendingCount = 0
        descendingCount = 0

        # Loop to find cost for ascension
        for i in range(len(nums)):
            ascendingCount += abs(nums[i] - ascendingNums[0 - i - 1])
        
        # Loop to find cost of descension
        for i in range(len(nums)):
            descendingCount += abs(nums[i] - descendingNums[0 - i - 1])
        
        return min(ascendingCount, descendingCount)
