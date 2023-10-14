import unittest
from src.board import Board


class TestBoard(unittest.TestCase):

    def test_board_creation(self):
        board = Board()
        self.assertEqual(board.width, 10)
        self.assertEqual(board.height, 10)
