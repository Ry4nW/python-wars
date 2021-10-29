class Solution:
    def solve(self, nums):
        count = len(nums)
        encountered = {}

        for i in nums:
            if i not in encountered:
                encountered[i] = 1
            else:
                count += encountered[i]
                encountered[i] += 1
        
        return count
