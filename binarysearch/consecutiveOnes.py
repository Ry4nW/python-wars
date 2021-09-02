class Solution:
    def solve(self, nums):

        for i in range(nums.index(1), len(nums)):

            if nums[i] != 1:

                if 1 in nums[i:]:
                    return False
                
                return True
        
        return True
        