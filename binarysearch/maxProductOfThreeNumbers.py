import numpy

class Solution:
    def solve(self, nums):

        nums.sort()
        nums = list(set(nums))
        return max(numpy.prod(list[:-3], numpy.prod(list[:2], list[0])))
        