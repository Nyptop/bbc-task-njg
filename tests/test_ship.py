import unittest
from src.ship import Ship


class TestShip(unittest.TestCase):

    def test_valid_orientations(self):
        try:
            Ship(3, 'horizontal')
            Ship(4, 'vertical')
        except ValueError:
            self.fail("Unexpected ValueError for valid orientations")

    def test_invalid_orientation_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            Ship(3, 'diagonal')
        self.assertEqual(
            str(context.exception),
            "Invalid orientation 'diagonal'. Must be one of ['horizontal', 'vertical']",
        )
