class Solution:
    def solve(self, nums):

        counts = collections.Counter(nums)
        return sorted(nums, key=lambda x: (counts[x], x), reverse=True)
        