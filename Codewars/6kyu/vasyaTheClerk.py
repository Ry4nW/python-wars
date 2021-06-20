def tickets(people):

    cash = 0

    for i in people:
        
        if i > 25 and (i - 25) > cash:
            return 'NO'
    
        cash += i

    # Check for bill amounts
    
    return 'YES'
