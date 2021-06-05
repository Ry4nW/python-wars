def get_length_of_missing_array(arr):

    if len(arr) == 0:
        return 0
    else:

        lens = []

        for i in arr:
            if i == None or len(i) == 0:
                return 0
            
            lens.append(len(i))
        

        lens.sort()
        prevInt = 0

        for i in lens:
            if (prevInt == 0):
                prevInt = i
                continue
                
            if (i - 1 > prevInt):
                return prevInt + 1
            
            prevInt = i
            
    return 0


print(get_length_of_missing_array([[5, 2, 9], [4, 5, 1, 1], [1], [69, 69], [5, 6, 7, 8, 9]]))
