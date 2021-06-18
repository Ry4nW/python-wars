# RLE is a simple form of data compression in which types of data are
# stored as the single value and its amount.

# e.g. AAABBBCCCD ---> 3A3B3C1D
# e.g. 3A ---> AAA 

def encode(string):

    encodedStr = ''
    data = string[0]
    count = 0

    for i in range(len(string)):

        if string[i] == data:
            count += 1

        else:

            data = string[i]
            encodedStr += "{count}".format(count=count) + string[i - 1]
            count = 1

        if i == len(string) - 1:
            c = str(count)
            encodedStr += c + data

    return "{count}".format(count=count) + data if len(encodedStr) == 0 else encodedStr


def decode(string):

    decodedString = ''
    num = ''

    for i in range(len(string)):

        if string[i].isnumeric():
            num += string[i]

        else:

            for _ in range(int(num)):
                decodedString += string[i]

            num = ''

    return decodedString
