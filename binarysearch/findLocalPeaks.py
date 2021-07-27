class Solution:
    def solve(self, nums):

        peaks = []

        try:
            if nums[0] > nums[1]:
                peaks.append(0)
        except:
            return []

        for i in range(1, len(nums) - 1):
            
            if nums[i - 1] < nums[i] > nums[i + 1]:
                peaks.append(i)
        
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            peaks.append(len(nums) - 1)


        return peaks