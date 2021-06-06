def rot13(message):
    
    alph = 'abcdefghijklmnopqrstuvwxyz'
    encodedMessage = ''
    
    for i in message:
        for j in range(len(alph)):
            
            if alph[j] == i:
                encodedMessage += alph[j + 13] 
                break
                
    # code to check for out of range, extend back to beginning of alphabet
    # also check for and match the message letter's casing
    
    return encodedMessage
                