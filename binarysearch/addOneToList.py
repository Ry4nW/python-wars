class Solution:
    def solve(self, nums):

        return [int(x) for x in list(str(int(''.join([str(num) for num in nums])) + 1))]
        