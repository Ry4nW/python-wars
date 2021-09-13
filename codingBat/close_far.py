def close_far(a, b, c):
    
    if (abs(a - b) > 1 and abs(c - b)) == 1 or (abs(a - c) == 1 and abs(b - c) > 1): return True
    return False
    