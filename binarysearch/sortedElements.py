class Solution:
    def solve(self, nums):

        sameIndexAfterSortingCount = 0

        sortedNums = sorted(nums)

        for i in range(len(nums)):

            if sortedNums[i] == nums[i]:
                sameIndexAfterSortingCount += 1
        
        return sameIndexAfterSortingCount
        