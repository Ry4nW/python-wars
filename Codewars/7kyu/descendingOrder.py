def descending_order(num):
    strNum = str(num)
    nums = []
    
    for i in range(len(strNum)):
        nums.append(int(strNum[i]))
        
    nums.sort()
    nums.reverse()
    returnNum = ''
    
    for i in nums:
        returnNum += str(i)

    return int(returnNum)

# One-liner:

def descending_order2(num):
    return int("".join(sorted(str(num), reverse=True)))

# sorted() takes an iterable and can take an optional boolean for reversal. Returns a list.
