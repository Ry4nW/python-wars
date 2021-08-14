class Solution:
    def solve(self, nums):

        missingNums = []
        dummyValues = [1 for x in range(len(nums))]
        iterator = iter(nums)
        numsDict = dict(zip(iterator, dummyValues))

        for i in range(1, len(nums) + 1):

            if i not in numsDict:
                missingNums.append(i)
        
        return sorted(missingNums)
        