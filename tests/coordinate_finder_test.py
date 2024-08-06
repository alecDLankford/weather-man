import unittest
from helpers.coordinate_finder import get_coordinates

class TestCooridinateFinder(unittest.TestCase):

    def test_valid_location(self):
        city = "Dallas"
        state = "Texas"

        result = get_coordinates(city,state)

        self.assertEqual(result,(32.7762719, -96.7968559))

    def test_invalid_location(self):
        city = "THISDOESNOTEXIST"
        state = "THISALSODOESNOTEXIST"

        result = get_coordinates(city, state)

        self.assertEqual(result, (None, None))

    def test_empty_input(self):
        city = ""
        state = ""

        result = get_coordinates(city, state)

        self.assertEqual(result, (None, None))
