def points(games):
    score = 0

    for i in games:
        if i[0] > i[2]:
            score += 3
        elif i[0] < i[2]:
            continue
        else:
            score += 1
    
    return score

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))

