def find_outlier(integers):

    evenCount = 0
    oddCount = 0

    for i in range(0, 3):

        if integers[i] % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1

    if evenCount > oddCount:

        for i in integers:

            if i % 2 != 0:
                return i
    else:

         for i in integers:

            if i % 2 == 0:
                return i

# 3 liner

def find_outlier2(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
    