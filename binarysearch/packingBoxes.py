class Solution:
    def solve(self, nums):

        deliveryTruck = []

        try:
            currentBox = [nums[0]]
        except:
            return nums

        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1]:
                currentBox.append(nums[i])
            else:
                deliveryTruck.append(currentBox)
                currentBox = [nums[i]]

        deliveryTruck.append(currentBox)
        
        return deliveryTruck
        