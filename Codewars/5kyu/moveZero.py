def move_zeros(array):
    numArr = []
    zeroCount = 0
    
    for i in array:
        
        if i != 0:
            numArr.append(i)
        else:
            zeroCount += 1
            
    for i in range(zeroCount):
        numArr.append(0)
        
    return numArr

print(move_zeros([1, 0]))
# One-liner:

def move_zeros2(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
