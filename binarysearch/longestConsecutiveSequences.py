class Solution:
    def solve(self, nums):

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        nums.sort()
        consecutiveNumCount = 0
        currentCount = 0
        elsed = False

        for i in range(len(nums) - 1):

            if nums[i + 1] == nums[i] + 1:
                currentCount += 1
            elif nums[i + 1] == nums[i]:
                continue
            elif currentCount != 0:

                elsed = True
                currentCount += 1

                if currentCount > consecutiveNumCount:
                    consecutiveNumCount = currentCount

                currentCount = 0
        
        if nums[-1] == nums[-2] + 1 and len(nums) > 2:
            print('h')
            currentCount += 1
            consecutiveNumCount += 1
            return consecutiveNumCount if currentCount < consecutiveNumCount else currentCount
        
        if elsed:
            print('e')
            return consecutiveNumCount if currentCount < consecutiveNumCount else currentCount
        
        return consecutiveNumCount + 1 if consecutiveNumCount + 1 > currentCount + 1 else currentCount + 1
        
