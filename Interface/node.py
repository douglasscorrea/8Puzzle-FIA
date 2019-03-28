class Node():
    def __init__(self, upper, value, depth, board=None):
        self.upper = upper
        self.value = value
        self.lowers = []
        self.depth = depth
        self.board = board
        self.h_cost = 0

    def get_lowers(self):
        return self.lowers

    def append_lower(self, node):
        self.lowers.append(node)

    def get_upper(self):
        return self.upper

    def set_uppers(self, node):
        self.upper = node

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_depth(self):
        return self.depth

    def set_depth(self, depth):
        self.depth = depth

    def set_board(self, b):
        self.board = b

    def get_board(self):
        return self.board

    def get_h_cost(self):
        return self.h_cost

    def set_h_cost(self, cost):
        self.h_cost = cost
