class Solution:
    def solve(self, s):

        allNumbers = []
        currentNumber = ''

        for i in str(s):

            if i.isdigit():
                currentNumber += i

            elif len(currentNumber) > 0:
                
                print(currentNumber)
                allNumbers.append(int(currentNumber)) 
                currentNumber = ''
        
        if len(currentNumber) > 0:
            allNumbers.append(int(currentNumber))

        return sum(allNumbers)
