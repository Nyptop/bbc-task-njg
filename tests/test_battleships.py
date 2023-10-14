import unittest
from src.board import Board
from src.ship import Ship
from src.player import Player


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

    def test_horizontal_ships_do_not_overlap(self):
        board = Board()
        ship1 = Ship(3, 'horizontal')
        ship2 = Ship(2, 'horizontal')

        board.place_ship(ship1, (2, 3))

        # Try to overlap second ship with first
        try:
            board.place_ship(ship2, (3, 3))
            self.fail("Expected an exception due to overlapping ships")
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_ships_do_not_overlap_one_horizontal_one_vertical(self):
        board = Board()
        ship1 = Ship(4, 'horizontal')
        ship2 = Ship(4, 'vertical')

        board.place_ship(ship1, (2, 3))

        try:
            board.place_ship(ship2, (5, 3))
            self.fail("Expected an exception due to overlapping ships")
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_vertical_ships_do_not_overlap_at_ends(self):
        board = Board()
        ship1 = Ship(4, 'vertical')
        ship2 = Ship(4, 'vertical')

        board.place_ship(ship1, (2, 3))

        try:
            board.place_ship(ship2, (2, 6))
            self.fail("Expected an exception due to overlapping ships")
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_ship_cannot_be_placed_off_board_horizontally(self):
        board = Board()
        ship = Ship(4, 'horizontal')

        try:
            board.place_ship(ship, (8, 3))
            self.fail("Expected an exception for placing the ship off the board horizontally")
        except Exception as e:
            self.assertIsInstance(e, ValueError)

    def test_ship_cannot_be_placed_off_board_vertically(self):
        board = Board()
        ship = Ship(4, 'vertical')

        try:
            board.place_ship(ship, (3, 8))
            self.fail("Expected an exception for placing the ship off the board vertically")
        except Exception as e:
            self.assertIsInstance(e, ValueError)

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

    def test_ship_is_sunk_after_all_cells_hit(self):
        board = Board()
        ship_length = 3
        ship = Ship(ship_length, 'horizontal')
        start_position = (2, 3)
        board.place_ship(ship, start_position)

        # Hit all cells
        for i in range(ship_length):
            attack_position = (start_position[0] + i, start_position[1])
            board.attack(attack_position)

        self.assertTrue(ship.is_sunk(), "Expected the ship to be sunk")

    def test_ship_not_sunk_when_same_cell_hit_multiple_times(self):
        board = Board()
        ship_length = 3
        ship = Ship(ship_length, 'horizontal')
        start_position = (2, 3)
        board.place_ship(ship, start_position)

        # Hit the same cell of the ship multiple times
        attack_position = (2, 3)
        for _ in range(ship_length):
            board.attack(attack_position)

        self.assertFalse(ship.is_sunk(), ("Ship should not be sunk when "
                                          "the same cell is hit multiple times"))

    def test_all_ships_sunk_returns_false_when_not_all_ships_are_sunk(self):
        board = Board()

        ship1 = Ship(3, 'horizontal')
        ship2 = Ship(2, 'vertical')

        board.place_ship(ship1, (2, 3))
        board.place_ship(ship2, (4, 4))

        # Sink only the first ship
        for i in range(3):
            board.attack((2 + i, 3))

        self.assertFalse(board.all_ships_sunk(), "Expected not all ships to be sunk")

    def test_all_ships_sunk_returns_true_when_all_ships_are_sunk(self):
        board = Board()

        ship1 = Ship(3, 'horizontal')
        ship2 = Ship(2, 'vertical')
        ship3 = Ship(4, 'horizontal')

        board.place_ship(ship1, (2, 3))
        board.place_ship(ship2, (4, 4))
        board.place_ship(ship3, (6, 6))

        # Sink all ships
        for i in range(3):
            board.attack((2 + i, 3))

        for i in range(2):
            board.attack((4, 4 + i))

        for i in range(4):
            board.attack((6 + i, 6))

        self.assertTrue(board.all_ships_sunk(), "Expected all ships to be sunk")

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
