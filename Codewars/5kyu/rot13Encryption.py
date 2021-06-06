def rot13(message):
    
    alph = 'abcdefghijklmnopqrstuvwxyz'
    encodedMessage = ''
    
    for i in message:
        
        for j in range(len(alph)):
            
            found = False
            
            if alph[j].lower() == i.lower():
                
                try:
                    
                    if i == alph[j].upper():
                        encodedMessage += alph[j + 13].upper() 
                        found = True
                        break
                    
                    encodedMessage += alph[j + 13]
                    found = True
                    break
                    
                except IndexError:
                    
                    length = 13 - (len(alph[j:]))
                    
                    if i == alph[j].upper():
                        
                        encodedMessage += alph[length].upper()
                        found = True
                        break
                    
                    encodedMessage += alph[length]
                    found = True
                    break
    
        if found != True:
            encodedMessage += i
            
                
    return encodedMessage
                