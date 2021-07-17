def oddNumberOfDigits(nums):

        oddNumberOfDigitsCount = 0

        for i in nums:

            if len(str(i)) % 2 != 0:
                oddNumberOfDigitsCount += 1
        
        return oddNumberOfDigitsCount