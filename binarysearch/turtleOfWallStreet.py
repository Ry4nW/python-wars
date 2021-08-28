class Solution:
    def solve(self, nums):

        buys = []
        try:
            maxPrice = sorted(nums)[-1]
        except:
            return 0
        pronfits = 0
        
        for i in range(len(nums)):

            if nums[i] != maxPrice:
                buys.append(nums[i])
            else:
                pronfits += len(buys) * maxPrice - sum(buys)
                buys.clear()
                try:
                    maxPrice = sorted(nums[i + 1:])[-1]
                except:
                    break
        
        return pronfits 
