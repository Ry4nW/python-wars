# Any letter not within a-m is considered a color error.

def printer_error(string):

    invalidityCount = 0
    validColors = 'abcdefghijklm'

    for i in string:
        if i not in validColors:
            
            invalidityCount += 1

    return f'{invalidityCount}/{str(len(string))}'

# One-liner:

def printer_error2(string):

    return '{}/{}'.format(len([j for j in string if j not in 'abcdefghijklm']), len(string))
