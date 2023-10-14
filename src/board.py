class Board:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.grid = {}
        self.attacked_positions = set()

    def place_ship(self, ship, position):
        x, y = position
        if ship.orientation == 'horizontal':
            for i in range(ship.length):
                self.grid[(x + i, y)] = ship
        elif ship.orientation == 'vertical':
            for i in range(ship.length):
                self.grid[(x, y + i)] = ship

    def get_ship_at(self, position):
        return self.grid.get(position, None)

    def attack(self, position):
        ship = self.grid.get(position, None)
        if position in self.attacked_positions:
            return 'already attacked'
        self.attacked_positions.add(position)

        if ship is None:
            return 'miss'
        else:
            ship.hits += 1
            return 'hit'
