def count(string):
    charDict = {}
    
    for i in string:
        found = False
        
        for key in charDict:
            
            if i == key:
                charDict[key] += 1
                found = True
                break
    
        if found != True:
            charDict[i] = 1
            
    return charDict

# With {Counter()}

from collections import Counter

def count2(string):

    Counter(string)

# One-liner with .count()

def count3(string):

    return {i: string.count(i) for i in string}