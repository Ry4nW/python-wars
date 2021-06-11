# Takes 2 numbers, iterates through the range of the two,
# returns a list of numbers containing the property of:
# "The sum of all digits of the number raised to the 
# consecutive powers results in the same number."

def sum_dig_pow(a, b): 

    eurekaNums = []

    for i in range(a, b + 1):

        if i <= 9 and i >= 1:
            eurekaNums.append(i)
        else:

            numStr = str(i)

            for j in range(len(numStr)):
                if j 