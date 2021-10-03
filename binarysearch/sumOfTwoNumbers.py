class Solution:
    def solve(self, nums, k):
        
        sumDict = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            if k - nums[i] in sumDict and sumDict[k - nums[i]] != i:
                return True
        
        return False
        