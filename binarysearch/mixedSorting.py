class Solution:
    def solve(self, nums):

        evens = []
        odds = []

        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
        
        evens.sort()
        odds.sort(reverse = True)
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = evens[0]
                evens.pop(0)
            else:
                nums[i] = odds[0]
                odds.pop(0)
        
        return nums
        