def in_array(arr1, arr2):

    r = []

    for i in arr1:
        found = False

        for j in range(len(arr2)):
            
            for y in range(len(arr2[j])):
                
                if arr2[j][y] == i[0]:
                    if arr2[j][y:len(i)] == i:
                        
                        found = True
                        r.append(i)
                        break
                        
                    elif (y + len(i)) == len(arr2[j]) :
                        if arr2[j][y:len(i) + 3] == i:
                            
                            found = True
                            r.append(i)
                            break
                            
            if found:
                break
                           
    return sorted(r)

# Auto looping with "if {i} in {j}"

def in_array2(arr1, arr2):

    r = []

    for a1 in arr1:
        for a2 in arr2:

            if a1 in a2 and not a1 in r:
                r.append(a1)

    r.sort()

    return r



