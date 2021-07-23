def largestGap(nums):
    
        difference = 0
        sortedNums = sorted(nums)

        for i in range(len(sortedNums) - 1):

            if (sortedNums[i + 1] - sortedNums[i]) > difference:
                difference = sortedNums[i + 1] - sortedNums[i]
        
        return difference