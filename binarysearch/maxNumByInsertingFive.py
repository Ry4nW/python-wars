import math

class Solution:
    def solve(self, n):

        numString = str(n)
        possibilities = []
        currentCheck = 0

        for i in range(len(numString) + 1):

            try:
                currentCheck = int(numString[0:i] + '5' + numString[i:])
            except:

                try:
                    currentCheck = int('-' + str(abs(int(numString[0:i]))) + '5' + str(abs(int(numString[i:]))))
                except:
                    currentCheck = int('-5' + str(abs(int(numString[i:]))))
            
            possibilities.append(currentCheck)

        ret = -math.inf

        for num in possibilities:
            ret = max(ret, num)

        return ret
      