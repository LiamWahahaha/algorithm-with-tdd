import unittest

from sorting.merge_sort import merge_sort


class TestSortingAlgorithms(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(sorted([6, 3, 8, 7, 4, 1, 2, 9, 5, 0]), merge_sort([6, 3, 8, 7, 4, 1, 2, 9, 5, 0]))


if __name__ == '__main__':
    unittest.main()
