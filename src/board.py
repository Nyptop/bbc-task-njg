class Board:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.grid = {}

    def place_ship(self, ship, position):
        x, y = position
        if ship.orientation == 'horizontal':
            for i in range(ship.length):
                self.grid[(x + i, y)] = ship

    def get_ship_at(self, position):
        return self.grid.get(position, None)
