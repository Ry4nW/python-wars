# Takes 2 numbers, returns a list of numbers
# within that range containing the property of:
# "Sum of all digits of the number raised to the 
# consecutive powers results in the same number."

# e.g. 89 --> 8^1 + 9^2 === 89
# ^Eureka number.

def sum_dig_pow(a, b): 

    eurekaNums = []

    for i in range(a, b + 1):

        if i <= 9 and i >= 1:
            eurekaNums.append(i)
        else:

            numStr = str(i)
            sum = 0

            for j in range(len(numStr)):
                sum += int(numStr[j]) ** (j + 1)
            
            if sum == int(numStr):
                eurekaNums.append(i)

    return eurekaNums
