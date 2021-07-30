class Solution:
    def solve(self, nums):

        for i in range(len(nums)):

            nums[i] = nums[i] ** 2

        nums.sort()

        return nums
