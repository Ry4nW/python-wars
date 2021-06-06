def open_or_senior(data):

    categories = []
    
    for i in range(len(data)):

        if data[i][0] >= 55 and data[i][1] > 7:
            categories.append('Senior')
            continue
        
        categories.append('Open')

    return categories

# Nice one-liner:

def openOrSenior2(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]