def add_Binary(a,b):

    total = a + b
    binary = []

    while (total > 0):
        binary.append(total % 2)
        total //= 2
   
    binaryTotal = ""
    binary.reverse()

    for i in binary:
        binaryTotal += str(i)

    return binaryTotal

print(add_Binary(1,1))

def add_Binary_Easy(a, b):
    return bin(a + b)[2:] #bin() returns '0b<binary>' indicating thats its a binary

