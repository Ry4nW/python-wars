# Iterating thorugh a dict of letters, relatively slow
def aUniqueString(s):
    
        alphString = 'abcdefghijklmnopqrstuvwxyz'
        alph = {}

        for i in alphString:

            alph[i] = 0

        for i in s:

             alph[i] = alph[i] + 1
        
        for i in alph:

            if alph[i] > 1:
                return False

        return True

# Iterating through string with each character, slightly faser
def aUniqueString2(s):

        for i in range(len(s)):

            for j in range(i + 1, len(s)):

                if s[j] == s[i]:
                    return False
        
        return True

# Use sorted() to place the same letters together
def aUniqueString3(s):

    sorted(s)

    for i in range(len(s) - 1): # The length of string - 1 so we won't get IndexOutOfBounds on the last iteration

        if s[i] == s[i + 1]:
            return False

    return True



