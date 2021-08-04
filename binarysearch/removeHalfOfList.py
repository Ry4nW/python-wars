class Solution:
    def solve(self, nums):

        halfAmount = 0
        
        if len(nums) % 2 == 0:
            halfAmount = len(nums) / 2
        else:
            halfAmount = (len(nums) // 2) + 1

        uniqueNums = {}

        counts = collections.Counter(nums)
        sortedNums = sorted(nums, key=lambda x: (counts[x] , x), reverse = True)

        for i in range(len(sortedNums[:int(halfAmount)])):
            try:
                uniqueNums[sortedNums[i]] += 1
            except:
                uniqueNums[sortedNums[i]] = 0
        
        return len(uniqueNums) if len(uniqueNums) != 0 else 1
        