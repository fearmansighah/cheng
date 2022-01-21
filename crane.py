from operator import truediv


class Crane():

    def __init__(self):
        # initial settings
        self.holding_box = False # how to link with subsequent process
        self.position = 0

    def check_stack_state(self, stack):
        if stack.size == 0:
            stack.state = 'empty'
        elif stack.size == 4:
            stack.state = 'full'
        elif stack.size > 0 and self.size < 4:
            stack.state = 'safe'


    def mov_left(self):
        if self.position > 0 and self.position <= 6:
            self.position -= 1
                    
        else:
            pass
        

    def mov_right(self):
        if self.position >= 0 and self.position < 6:
            self.position += 1
                    
        else:
            pass


    def lift_box(self, stack):
        self.check_stack_state(stack)
        if self.holding_box == True:
            if stack.state == 'safe' or stack.state == 'full':
                stack.decBox()
        else:
            pass


    def drop_box(self, stack):
        self.check_stack_state(stack)
        if self.holding_box == False:
            if stack.state == 'safe' or 'empty':
                stack.addBox()
        else:
            pass


    def movement(self, mov_code, stack):
        if mov_code != 0:
            
            if mov_code == 1:
                self.mov_left()
            if mov_code == 2:
                self.mov_right()
            if mov_code == 3:
                self.lift_box(stack)
            if mov_code == 4:
                self.drop_box(stack)    

        else:
            pass
                
