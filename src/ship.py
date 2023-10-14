class Ship:
    def __init__(self, length, orientation):
        self.length = length
        self.orientation = orientation

    def place_ship(self, ship, position):
        self.grid[position] = ship

    def get_ship_at(self, position):
        return self.grid.get(position, None)
