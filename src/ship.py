class Ship:
    def __init__(self, length, orientation):
        self.length = length
        self.orientation = orientation
        self.hits = 0

    def is_sunk(self):
        return self.hits >= self.length
