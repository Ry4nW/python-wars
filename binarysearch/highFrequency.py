import collections

class Solution:
    def solve(self, nums):
        
        counter = collections.Counter(nums)
        mostCommon = counter.most_common(1)
        try:
            return mostCommon[0][1]
        except:
            return 0
            