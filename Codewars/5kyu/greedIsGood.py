def score(dice):

    points = 0
    numCount = 0
    
    for i in dice:

        numCount += 1

        if numCount == 3:
            points += int(str(i) + '00') if i != 1 else int(str(points) + '000')
            numCount = 0
        elif (dice.index(i) - 1) != i and (dice.index(i) != 0):
            points += 100 if i == 1 else 50 
            numCount = 0

    return points
