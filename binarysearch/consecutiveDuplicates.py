def consecutiveDuplicates(s):

    unduplicatedString = ''

    for i in range(len(s) - 1):

        if s[i + 1] != s[i]:
            unduplicatedString += s[i]

    try:
        unduplicatedString += s[-1]
    except:
        return unduplicatedString

    return unduplicatedString
