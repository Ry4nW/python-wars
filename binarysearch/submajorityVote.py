class Solution:
    def solve(self, nums):

        counts = Counter(nums)
        submajority = len(nums) // 3 + 1
        submajorCands = []

        for count in counts:
            if counts[count] >= submajority:
                submajorCands.append(count)
        
        return sorted(submajorCands)
        