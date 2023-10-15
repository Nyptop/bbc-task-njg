import unittest
from src.board import Board
from src.ship import Ship


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def place_ship(self, length, orientation, start_position):
        ship = Ship(length, orientation)
        self.board.place_ship(ship, start_position)
        return ship

    def test_board_creation(self):
        self.assertEqual(self.board.width, 10, "Board width not initialized correctly.")
        self.assertEqual(self.board.height, 10, "Board height not initialized correctly.")

    def test_place_ship_at_position(self):
        self.place_ship(4, 'horizontal', (3, 4))
        self.assertIsNotNone(self.board.get_ship_at((3, 4)), "No ship found at specified position.")

    def test_horizontal_ship_occupies_correct_cells(self):
        ship_length = 3
        start_position = (2, 3)
        self.place_ship(ship_length, 'horizontal', start_position)
        for i in range(ship_length):
            position = (start_position[0] + i, start_position[1])
            self.assertIsNotNone(self.board.get_ship_at(position),
                                 f"No ship found at position {position}")

    def test_vertical_ship_occupies_correct_cells(self):
        ship_length = 3
        start_position = (2, 3)
        self.place_ship(ship_length, 'vertical', start_position)
        for i in range(ship_length):
            position = (start_position[0], start_position[1] + i)
            self.assertIsNotNone(self.board.get_ship_at(position),
                                 f"No ship found at position {position}")

    def test_horizontal_ships_do_not_overlap(self):
        self.place_ship(3, 'horizontal', (2, 3))
        with self.assertRaises(ValueError) as context:
            self.place_ship(2, 'horizontal', (3, 3))
        self.assertEqual(str(context.exception), "Ships cannot overlap")

    def test_ships_do_not_overlap_one_horizontal_one_vertical(self):
        self.place_ship(4, 'horizontal', (2, 3))
        with self.assertRaises(ValueError) as context:
            self.place_ship(4, 'vertical', (5, 3))
        self.assertEqual(str(context.exception), "Ships cannot overlap")

    def test_vertical_ships_do_not_overlap_at_ends(self):
        self.place_ship(4, 'vertical', (2, 3))
        with self.assertRaises(ValueError) as context:
            self.place_ship(4, 'vertical', (2, 6))
        self.assertEqual(str(context.exception), "Ships cannot overlap")

    def test_ship_cannot_be_placed_off_board_horizontally(self):
        with self.assertRaises(ValueError) as context:
            self.place_ship(4, 'horizontal', (8, 3))
        self.assertEqual(str(context.exception), "Ship cannot be placed off the board horizontally")

    def test_ship_cannot_be_placed_off_board_vertically(self):
        with self.assertRaises(ValueError) as context:
            self.place_ship(4, 'vertical', (3, 8))
        self.assertEqual(str(context.exception), "Ship cannot be placed off the board vertically")

    def test_attack_empty_cell_results_in_miss(self):
        attack_result = self.board.attack((5, 5))
        self.assertEqual(attack_result, 'miss', f"Expected 'miss', got {attack_result}")

    def test_attack_ship_cell_results_in_hit(self):
        self.place_ship(3, 'horizontal', (2, 3))
        attack_result = self.board.attack((2, 3))
        self.assertEqual(attack_result, 'hit', f"Expected 'hit', got {attack_result}")

    def test_ship_is_sunk_after_all_cells_hit(self):
        ship_length = 3
        ship = self.place_ship(ship_length, 'horizontal', (2, 3))
        for i in range(ship_length):
            self.board.attack((2 + i, 3))
        self.assertTrue(ship.is_sunk(), "Expected the ship to be sunk")

    def test_ship_not_sunk_when_same_cell_hit_multiple_times(self):
        ship_length = 3
        ship = self.place_ship(ship_length, 'horizontal', (2, 3))
        for _ in range(ship_length):
            self.board.attack((2, 3))
        self.assertFalse(ship.is_sunk(), ("Ship should not be sunk when the same cell"
                                          " is hit multiple times"))

    def test_all_ships_sunk_returns_false_when_not_all_ships_are_sunk(self):
        self.place_ship(3, 'horizontal', (2, 3))
        self.place_ship(2, 'vertical', (4, 4))
        for i in range(3):
            self.board.attack((2 + i, 3))
        self.assertFalse(self.board.all_ships_sunk(), "Expected not all ships to be sunk")

    def test_all_ships_sunk_returns_true_when_all_ships_are_sunk(self):
        self.place_ship(3, 'horizontal', (2, 3))
        self.place_ship(2, 'vertical', (4, 4))
        for i in range(3):
            self.board.attack((2 + i, 3))
        for i in range(2):
            self.board.attack((4, 4 + i))
        self.assertTrue(self.board.all_ships_sunk(), "Expected all ships to be sunk")
