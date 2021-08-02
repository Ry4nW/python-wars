class Solution:
    def solve(self, nums):
        
        sortedList = []
        sortedNums = sorted(nums)

        if len(nums) % 2 == 0:
            while len(sortedNums) != 0:

                sortedList.append(sortedNums[-1])
                sortedList.append(sortedNums[0])

                del sortedNums[-1], sortedNums[0]
        else:
            while len(sortedNums) != 1:

                sortedList.append(sortedNums[-1])
                sortedList.append(sortedNums[0])

                del sortedNums[-1], sortedNums[0]

            sortedList.append(sortedNums[0])
        
        return sortedList
        