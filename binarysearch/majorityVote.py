class Solution:
    def solve(self, nums):
        counts = Counter(nums)
        majority = len(nums) // 2 + 1
        
        for count in counts:
            if counts[count] >= majority:
                return count
        
        return -1
        