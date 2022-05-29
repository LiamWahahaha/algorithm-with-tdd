import unittest

from stack.monotonic_stack import find_buildings


class MyTestCase(unittest.TestCase):
    def test_find_building(self):
        self.assertEqual([0, 2, 3], find_buildings([4, 2, 3, 1]))
        self.assertEqual([0, 1, 2, 3], find_buildings([4, 3, 2, 1]))
        self.assertEqual([3], find_buildings([1, 3, 2, 4]))


if __name__ == '__main__':
    unittest.main()
