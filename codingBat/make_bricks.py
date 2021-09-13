def make_bricks(small, big, goal):
    
    if 5 * (goal // 5) + small >= goal:
        return True
    
    return False
    