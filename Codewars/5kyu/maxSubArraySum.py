def max_sequence(arr):

    isNegative = True

    for i in arr: 

        if i >= 0:
            isNegative = False

    if isNegative != False:
        return 0
    else:

        totalSum = 0
        tempSum = 0

        for i in range(len(arr)):

            for j in range(i, len(arr)):

                for y in range(i, j + 1):

                    tempSum += arr[y]
                
                if tempSum > totalSum:
                    totalSum = tempSum
                
                tempSum = 0
    
    return totalSum


                




        