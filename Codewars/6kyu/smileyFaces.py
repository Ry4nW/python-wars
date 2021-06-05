def countSmileys(arr):

    smileyCount = 0;

    if (len(arr) == 0):
        return 0
    else:
        for i in arr:
            if i[0] == ";" or i[0] == ":":

                if i[1] == "-" or i[1] == "~":

                     if i[2] == ")" or i[2] == "D":
                          smileyCount += 1

                elif i[1] == ")" or i[1] == "D":
                    smileyCount += 1


    return smileyCount

print(countSmileys([':)', ';(', ';}', ':-D']))
