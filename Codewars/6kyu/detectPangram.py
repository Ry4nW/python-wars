import string

def is_pangram(s):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    
    for i in s:
        
        for j in alphabet:
            
            if i.lower() == j and i not in letters:
                
                letters.append(i.lower())
                
    print(letters)
    return len(letters) == 26 