class Stack:
    def __init__(self, size, position):
        self.size = size
        self.position = position

        # either full, empty or safe
        self.state = ''
        if self.size >= 4:
            self.state = 'full'
        elif self.size == 0:
            self.state = 'empty'
        else:
            self.state == 'safe' 

    def addBox(self):
        self.size += 1

    def decBox(self):
        self.size -= 1

    