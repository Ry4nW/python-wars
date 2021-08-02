class Solution:

    #Attempt that TLEs but otherwise works. 
    def solve(self, nums, k, target):

        validSublistCount = 0
        count = 0

        while count + k <= len(nums):

            sublist = nums[count : count + k]

            if sum(sublist) / len(sublist) >= target:
                validSublistCount += 1

            count += 1
        
        return validSublistCount

    # Optimal answer using the Sliding Window method, by https://github.com/Prodyte
    def solve(self, nums, k, target):

        if len(nums) < k:
            return 0

        window_sum = sum(nums[:k])
        cnt = +(window_sum / k >= target)

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            if window_sum / k >= target:
                cnt += 1

        return cnt
