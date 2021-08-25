class Solution:
    def solve(self, nums, k):

        i = 0
        j = len(nums) - 1

        while i < j:

            curSum = nums[i] + nums[j]

            if curSum == k:
                return True
            elif curSum < k:
                i += 1
            else:
                j -= 1
        
        return False
