def order(sentence):

    wordList = sentence.split(' ')
    orderedWordList = ['' for _ in wordList]

    for i in range(len(wordList)):

        for j in wordList[i]:

            if j.isnumeric():

                orderedWordList[int(j) - 1] = wordList[i]
                break
    
    return ' '.join(orderedWordList)

