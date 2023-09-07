def initial_state():
    return (8, 0, 0)

def is_goal(s):
    x, y, z = s
    if x==4 and y==4:
        return True
    else:
        return False

def successors(s):
    x, y, z = s
    
    # Empty one bottle
    if x > 0:
        yield ((0, y, z), x)
    if y > 0:
        yield ((x, 0, z), y)
    if z > 0:
        yield ((x, y, 0), z)
        
    # Fill up one bottle
    if x < 3:
        yield ((3, y, z), 3-x)
    if y < 5:
        yield ((x, 5, z), 5-y)
    if z < 8:
        yield ((x, y, 8), 8-z)
        
    # Pour from one to another
    # 3L -> 5L
    t = 5-y
    if x > 0 and t > 0:
        if x > t:
            yield ((x-t, 5, z), t)
        else:
            yield ((0, y+x, z), x)
    # 3L -> 8L
    t = 8-z
    if x > 0 and t > 0:
        if x > t:
            yield ((x-t, y, 8), t)
        else:
            yield ((0, y, z+x), x)
            
    # 5L -> 3L
    t = 3-x
    if y > 0 and t > 0:
        if y > t:
            yield ((3, y-t, z), t)
        else:
            yield ((x+y, 0, z), y)
    
    # 5L -> 8L
    t = 8-z
    if y > 0 and t > 0:
        if y > t:
            yield ((x, y-t, 8), t)
        else:
            yield ((x, 0, z+t), y)
            
    # 8L -> 3L
    t = 3-x
    if z > 0 and t > 0:
        if z > t:
            yield ((3, y, z-t), t)
        else:
            yield ((x+z, y, 0), z)
            
    # 8L -> 5L
    t = 5-y
    if z > 0 and t > 0:
        if z > t:
            yield ((x, 5, z-t), t)
        else:
            yield ((x, y+z, 0), z)