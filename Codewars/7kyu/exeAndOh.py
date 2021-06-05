def xo(s):
    xcount = 0
    ocount = 0

    for i in s.lower():
        if (i == 'x'):
            xcount += 1
        elif (i == 'o'):
            ocount += 1
            
    return xcount == ocount

print(xo('ooxx'))

# Using count()

def xo2(s):
    s = s.lower()
    return s.count('x') == s.count('o')