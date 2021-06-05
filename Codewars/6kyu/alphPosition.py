def alphabet_position(text):
    
    positions = []
    alph = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in text:
        for j in range(len(alph)):
            
            if i.lower() == alph[j]:
                positions.append(str(j + 1))
                
    return ' '.join(positions)

