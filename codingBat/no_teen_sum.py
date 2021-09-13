def no_teen_sum(a, b, c):

    retSum = 0

    for i in [a, b, c]:
        if i <= 19 and i >= 13 and i != 15 and i != 16:
            continue
        retSum += i
    
    return retSum
    