

class Widget:

    FIXED_POSITION = 0 # to the screen
    ABSOLUTE_POSITION = 1 # to the container
    AUTO_BOTTOM = 2 # auto in the container
    AUTO_RIGHT = 3 # auto in the container

    def __init__(self, container):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.position_type = None
        self.container = None
        self.placed = False
        self.warn = True
        self.container = container

        # optionals
        self.absolute_position = [0, 0]
        self.fixed_position = [0, 0]

        # padding
        self.left_padding = 0
        self.right_padding = 0
        self.top_padding = 0
        self.bottom_padding = 0

        # margin
        self.left_margin = 0
        self.right_margin = 0
        self.top_margin = 0
        self.bottom_margin = 0
    
    def getTotalWidth(self):
        return self.w + self.left_margin + self.right_margin + self.left_padding + self.right_padding
    
    def getTotalHeight(self):
        return self.h + self.top_margin + self.bottom_margin + self.top_padding + self.bottom_padding


    def setMargins(self, left=0, right=0, top=0, bottom=0):
        if self.warn:
            if self.placed and self.position_type == Widget.AUTO_BOTTOM:
                print("Warning : Errors may occurs when resizing a widgets that is already placed in a container")
        self.left_margin = left
        self.right_margin = right
        self.top_margin = top
        self.bottom_margin = bottom
    
    def setPaddings(self, left=0, right=0, top=0, bottom=0):
        self.left_padding = left
        self.right_padding = right
        self.top_padding = top
        self.bottom_padding = bottom
