

class Widget:

    RELATIVE_POSITION = 0
    ABSOLUTE_POSITION = 1
    AUTO_POSITION = 2

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.position_type = None
        self.container = None
        self.placed = False
