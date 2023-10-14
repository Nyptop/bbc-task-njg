class Player:
    def __init__(self, board):
        self.board = board

    def has_lost(self):
        return self.board.all_ships_sunk()
