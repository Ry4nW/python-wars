class Solution:
    def solve(self, nums, target):
        nums.sort()
        query = target - nums[0] + 1
        lo, hi = 0, len(nums) - 1
        curSmallest = float('inf')

        while lo <= hi:
            mid = (lo + hi) // 2
            midNum = nums[mid]

            if midNum > query:
                if midNum < curSmallest:
                    curSmallest = midNum
                hi = mid - 1
            else:
                lo = mid + 1
        
        return curSmallest + nums[0]

solution = Solution()
print(solution.solve([0, 2, 2], 2))