def pig_it(txt):

    words = txt.split()
    pigWords = []

    for i in words:
        if i == '!' or i == '?':
            pigWords.append(i)
            continue
            
        word = ''

        word += i[1:]
        word += i[0]
        word += 'ay'

        pigWords.append(word)
        
    return ' '.join(pigWords)
    