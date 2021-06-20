def narcissistic(num):

    sum = 0
    iterableNum = str(num)

    for i in iterableNum:

        sum += int(i) ** len(iterableNum)

    return True if sum == num else False

# One-liner:

def narcissistic2(num):

    return num == sum(int(i) ** len(str(num)) for i in str(num))