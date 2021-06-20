def friend(x):
    
    friendList = []
    
    for i in x:
        friendList.append(i) if len(i) == 4 else None

    return friendList

# "Tenary" without {else} in list declaration needs to come
#  after loop, e.g.

def friend2(x):
    
    return [f for f in x if len(f) == 4]