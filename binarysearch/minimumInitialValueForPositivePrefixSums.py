# Attempt, TLEs on submission
class Solution:
    def solve(self, nums):

        if len(nums) == 0:
            return 1
        elif len(nums) == 1:
            return abs(nums[0]) + 1 if abs(nums[0]) != nums[0] else 1

        largestPrefixSum = float('inf')

        for i in range(1, len(nums) + 1):

            prefixSum = sum(nums[0 : i])

            if prefixSum < largestPrefixSum:
                largestPrefixSum = prefixSum
        
        if largestPrefixSum != 0:
            return abs(largestPrefixSum + -1) if abs(largestPrefixSum) != largestPrefixSum else 1 
        
        return 1
