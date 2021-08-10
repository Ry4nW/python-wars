class Solution:
    def solve(self, nums):

        values = {}

        for i in nums:

            if i in values:
                return i
            else:
                values[i] = 1
        