class Solution:
    def solve(self, nums):
        
        for i in range(2, len(nums), 4):

            try:
                holder = nums[i]
                nums[i] = nums[i - 2]
                nums[i - 2] = holder
            except:
                break

        for i in range(1, len(nums), 4):

            try:
                holder = nums[i]
                nums[i] = nums[i + 2]
                nums[i + 2] = holder
            except: 
                break

        return nums