class Solution:
    def solve(self, nums):

        integersDict = {}

        for i in range(len(nums)):

            try:
               integersDict[nums[i]] += 1

            except:
                integersDict[nums[i]] = 1

        for integer in integersDict:

            if integersDict[integer] != 3:
                return integer
        
        return nums[0]
        