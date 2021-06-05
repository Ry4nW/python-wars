def tower_builder(n_floors):
    
    floor = ''
    building = []
    tiles = 1

    
    # Build the top floor.
    for i in range(n_floors + 1):
        if i == 0:
            continue
            
        floor = ''
        
        floor += ' ' * (n_floors - i)
        floor += '*' * tiles
        floor += ' ' * (n_floors - i)
        
        tiles += 2
        
        building.append(floor)
    
        
    return building