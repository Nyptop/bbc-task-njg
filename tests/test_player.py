import unittest
from src.board import Board
from src.ship import Ship
from src.player import Player


class TestPlayer(unittest.TestCase):

    def test_player_loses_when_all_ships_are_sunk(self):
        board = Board()

        player = Player(board)

        ship1 = Ship(3, 'horizontal')
        ship2 = Ship(2, 'vertical')
        ship3 = Ship(4, 'horizontal')

        board.place_ship(ship1, (2, 3))
        board.place_ship(ship2, (4, 4))
        board.place_ship(ship3, (6, 6))

        for i in range(3):
            player.attack_position((2 + i, 3))

        for i in range(2):
            player.attack_position((4, 4 + i))

        for i in range(4):
            player.attack_position((6 + i, 6))

        self.assertTrue(player.has_lost(), "Expected the player to have lost")
