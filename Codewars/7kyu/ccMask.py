# return masked string

def maskify(cc):
    if cc == '':
        return ''
    elif len(cc) <= 4:
        return cc

    maskedString = ''
    count = 0

    for i in range(len(cc) - 1, -1, -1):
        maskedString += cc[i]
        count += 1

        if count >= 4:
            hashString = ''
            for j in range(len(cc) - 4):
                hashString += '#'

            return hashString + maskedString[::-1]


print(maskify("4556364607935616"))


# masked string simplified

def maskify2(cc):
    return "#" * (len(cc) - 4) + cc[-4:]

