class Board:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.grid = {}

    def place_ship(self, ship, position):
        self.grid[position] = ship

    def get_ship_at(self, position):
        return self.grid.get(position, None)
