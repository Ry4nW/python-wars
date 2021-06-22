def buddy(start, limit):

    add = 0
    mDivisorSum = 0
    nDivisorSum = 0
    

    if (limit > start):

        for n in range(start, limit + 1):
            
            nDivisorSum = 0

            # Gets divisors for i
            for j in range(1, n // 2 + 1):

                if type(n / j) != float:

                    nDivisorSum += 1

            # Loops while divisor sum is less than i
            while (mDivisorSum <= start + 1):

                mDivisorSum = 0
                m = n + add

                # Iterates through half of the number 
                # to obtain it's proper divisors
                for j in range(1, ((m) // 2) + 1):

                    if type(n / j) != float:

                        mDivisorSum += j

                if mDivisorSum == n + 1 and nDivisorSum == m + 1:

                    return [n, m]

                add += 1

    return 'Nothing'



                    