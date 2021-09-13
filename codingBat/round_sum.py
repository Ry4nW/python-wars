def round_sum(a, b, c):

    retSum = 0

    for i in [a, b, c]:
        curInt = int(str(i)[-1])

        if curInt >= 5:
            retSum += 10

        retSum += i - curInt
    
    return retSum
    