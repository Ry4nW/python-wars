class Solution:
    def solve(self, nums):

        for i in range(len(nums)):

            try:
                
                test = nums[2 * i + 1]
                test = 2 * i + 1

                if nums[i] < nums[test]:
                    return False
                elif nums[i] < nums[2 * i + 2]:
                    return False

            except:
                continue
        
        return True
        