class Solution:
    def solve(self, nums):

        try:
            curNum = nums[0]
        except:
            return nums
        numCount = 0
        i = 0

        while i != len(nums):

            if nums[i] != curNum:
                curNum = nums[i]

                if numCount > 2:
                    j = i - 1
                    while numCount != 2:
                        del nums[j]
                        j -= 1
                        numCount -= 1

                    i = j - 1
                
                numCount = 0
            
            numCount += 1
            i += 1
        
        if numCount > 2:

            j = len(nums) - 1

            while numCount != 2:
                del nums[j]
                j -= 1
                numCount -= 1   
    
        return nums
        