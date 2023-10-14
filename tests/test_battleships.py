import unittest
from src.board import Board
from src.ship import Ship


class TestBoard(unittest.TestCase):

    def test_board_creation(self):
        board = Board()
        self.assertEqual(board.width, 10)
        self.assertEqual(board.height, 10)

    def test_place_ship_at_position(self):
        board = Board()
        ship = Ship(4, 'horizontal')

        position = (3, 4)
        board.place_ship(ship, position)

        placed_ship = board.get_ship_at(position)

        self.assertIsNotNone(placed_ship, "No ship found at specified position")
