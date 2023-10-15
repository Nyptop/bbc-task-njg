class Player:
    """
    Represents a player in the Battleship game.

    A player can attack positions on their opponent's game board and have their own game board
    attacked. They can lose if all their ships are sunk.
    """

    def __init__(self, board):
        self.board = board

    def attack_position(self, position):
        return self.board.attack(position)

    def has_lost(self):
        return self.board.all_ships_sunk()
