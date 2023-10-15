class Board:
    """
    Represents the game board for Battleship.

    The board is a grid with a default size of 10x10 where ships can be placed.
    Players can attack specific positions on the board, and the board keeps track
    of which positions have been attacked.
    """

    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = {}
        self.attacked_positions = set()

    def place_ship(self, ship, position):
        x, y = position

        if ship.orientation == 'horizontal' and x + ship.length - 1 >= self.width:
            raise ValueError("Ship cannot be placed off the board horizontally")

        if ship.orientation == 'vertical' and y + ship.length - 1 >= self.height:
            raise ValueError("Ship cannot be placed off the board vertically")

        for i in range(ship.length):
            if ship.orientation == 'horizontal':
                new_position = (x + i, y)
            elif ship.orientation == 'vertical':
                new_position = (x, y + i)
            if self.grid.get(new_position, None) is not None:
                raise ValueError("Ships cannot overlap")

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

    def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in set(self.grid.values()))
