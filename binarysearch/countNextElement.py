class Solution:
    def solve(self, nums):

        setNums = set(nums)
        count = 0

        for i in setNums:
            if i + 1 in setNums:
                count += nums.count(i)
        
        return count
