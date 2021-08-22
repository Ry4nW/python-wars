class Solution:
    def solve(self, nums):
        
        numsDict = {}

        for i in nums:

            if i in numsDict:
                numsDict[i] += 1
            else:
                numsDict[i] = 1    
        
        for num in numsDict:
            if num == numsDict[num]:
                return True

        return False
        