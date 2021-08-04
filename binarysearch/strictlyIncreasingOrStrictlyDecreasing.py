class Solution:
    def solve(self, nums):

        if len(nums) == 1:
            return True

        increasing = False
        decreasing = False

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                increasing = True
                if increasing and decreasing:
                    return False
                else:
                    continue
            elif nums[i] < nums[i - 1]:
                decreasing = True
                if increasing and decreasing:
                    return False
                else:
                    continue
            
            return False
        
        return True 
            