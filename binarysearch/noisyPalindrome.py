def noiseyPalindrome(s):

    nonNoisyString = ''

    for i in s:

        if (i.isdigit() == False) and (i.lower() == i):

            nonNoisyString += i
        
    return nonNoisyString[::-1] == nonNoisyString

    