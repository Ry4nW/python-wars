class Solution:
    def solve(self, nums):

        occurrences = {}

        for i in set(nums):
            curCount = nums.count(i)
            if curCount in occurrences:
                return False
            
            occurrences[curCount] = 1
        
        return True
        