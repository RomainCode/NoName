

def isCollisionRect(x1, y1, x2, y2, w1, h1, w2, h2) -> bool:
    if x1 < x2+w2 and x1+w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2:
        return True
    return False
