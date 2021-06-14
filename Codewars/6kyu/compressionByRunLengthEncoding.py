# RLE is a simple form of data compression in which types of data are
# stored as the single value and its amount.

# e.g. AAABBBCCCD ---> 3A3B3C1D
# e.g. 3A ---> AAA 

def encode(str):

    encodedStr = ''
    data = str[0]
    count = 0

    for i in range(len(str)):

        if str[i] == data:
            count += 1

        else:
            
            data = str[i]
            encodedStr += "{count}".format(count = count) + str[i - 1]
            count = 1
            
            if i == len(str) - 1:
                encodedStr += "1" + str[i]
                break
    
    return "{count}".format(count = count) + data if len(encodedStr) == 0 else encodedStr 


def decode(str): 
    
    decodedStr = ''
    index = 0
    
    for i in str: 
        
        for _ in range(int(index)):
                
            decodedStr += str[i + 1]
            
        
    
    return decodedStr
                