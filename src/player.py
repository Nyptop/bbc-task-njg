class Player:
    def __init__(self, board):
        self.board = board

    def attack_position(self, position):
        return self.board.attack(position)

    def has_lost(self):
        return self.board.all_ships_sunk()
