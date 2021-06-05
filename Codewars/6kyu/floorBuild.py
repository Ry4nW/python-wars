def tower_builder(n_floors):
    
    floor = ''
    building = []
    tiles = 1

    
    # Build the top floor.
    for i in range(1, n_floors + 1):
            
        floor = ''
        
        floor += ' ' * (n_floors - i)
        floor += '*' * tiles
        floor += ' ' * (n_floors - i)
        
        tiles += 2
        
        building.append(floor)
    
        
    return building