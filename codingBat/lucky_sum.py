def lucky_sum(a, b, c):

    retSum = 0

    for i in [a, b, c]:
        if i == 13:
            break
        
        retSum += i
    
    return retSum
