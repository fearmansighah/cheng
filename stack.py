class Stack:
    def __init__(self, size, position, state, in_out_diff):
        self.size = size
        self.position = position
        self.state = state
        self.in_out_diff = in_out_diff

    def increase_size_by_1(self):
        self.size = self.size + 1

    def decrease_size_by_1(self):
        self.size = self.size - 1

    def increase_position_by_1(self):
        self.position = self.position + 1

    def decrease_position_by_1(self):
        self.position = self.position - 1

    def set_state(self, change_state):
        self.state = change_state
    
    def increase_diff_by_1(self):
        self.in_out_diff = self.in_out_diff + 1

    def decrease_diff_by_1(self):
        self.in_out_diff = self.in_out_diff - 1