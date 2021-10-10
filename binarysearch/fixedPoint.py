class Solution:
    def solve(self, nums):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            midPoint = nums[mid]

            if mid == midPoint:
                if mid - 1 >= 0 and nums[mid - 1] == midPoint - 1:
                    hi = mid - 1
                else:
                    return midPoint
            elif mid > midPoint:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1 
        