def narcissisticNumber(n):

        sum = 0
        length = len(str(n))

        for i in str(n):
            sum += int(i) ** length

        return sum == n