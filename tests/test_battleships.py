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

    def test_place_horizontal_ship_occupies_correct_cells(self):
        board = Board()
        ship_length = 3
        ship = Ship(ship_length, 'horizontal')

        start_position = (2, 3)
        board.place_ship(ship, start_position)

        for i in range(ship_length):
            position = (start_position[0] + i, start_position[1])
            placed_ship = board.get_ship_at(position)
            self.assertIsNotNone(placed_ship, f"No ship found at position {position}")

    def test_place_vertical_ship_occupies_correct_cells(self):
        board = Board()
        ship_length = 3
        ship = Ship(ship_length, 'vertical')

        start_position = (2, 3)
        board.place_ship(ship, start_position)

        for i in range(ship_length):
            position = (start_position[0], start_position[1] + i)
            placed_ship = board.get_ship_at(position)
            self.assertIsNotNone(placed_ship, f"No ship found at position {position}")

    def test_attack_empty_cell_results_in_miss(self):
        board = Board()

        attack_position = (5, 5)
        attack_result = board.attack(attack_position)

        self.assertEqual(attack_result, 'miss', f"Expected 'miss', got {attack_result}")

    def test_attack_ship_cell_results_in_hit(self):
        board = Board()
        ship = Ship(3, 'horizontal')
        start_position = (2, 3)
        board.place_ship(ship, start_position)

        attack_position = (2, 3)
        attack_result = board.attack(attack_position)

        self.assertEqual(attack_result, 'hit', f"Expected 'hit', got {attack_result}")
