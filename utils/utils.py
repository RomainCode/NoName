import math

def isCollisionRect(x1, y1, x2, y2, w1, h1, w2, h2) -> bool:
    if x1 < x2+w2 and x1+w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2:
        return True
    return False


def magnitude(x1, y1, x2, y2): # lenght of a vector
    return math.sqrt((x1+x2)**2 + (y1+y2)**2)

def isPointInRect(xr, yr, wr, hr, x, y) -> bool:
    x1, y1, w, h = xr, yr, wr, hr
    x2, y2 = x1+w, y1+h
    if (x1 < x and x < x2):
        if (y1 < y and y < y2):
            return True
    return False