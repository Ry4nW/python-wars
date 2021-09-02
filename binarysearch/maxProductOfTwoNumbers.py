class Solution:
    def solve(self, nums):

        if len(nums) < 2:
            return 0

        nums.sort()
        product1 = nums[-1] * nums[-2]
        product2 = nums[0] * nums[1]

        return product1 if product1 > product2 else product2 
        