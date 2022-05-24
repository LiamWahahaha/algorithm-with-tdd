import unittest

from dynamic_programming.house_robber import house_robber_top_down, house_robber_bottom_up, house_robber_ii_top_down
from dynamic_programming.longest_common_subsequence import calculate_lcs_length_top_down, \
    calculate_lcs_length_bottom_up, find_lcs, find_all_lcs


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_calculate_lcs_length(self):
        self.assertEqual(3, calculate_lcs_length_top_down("ABCDEF", "BCESA"))
        self.assertEqual(3, calculate_lcs_length_bottom_up("ABCDEF", "BCESA"))

    def test_find_lcs(self):
        self.assertIn(find_lcs("XMJYAUZ", "MZJAWXU"), {"MJAU"})
        self.assertIn(find_lcs("ABCBDAB", "BDCABA"), {"BCAB", "BCBA", "BDAB"})

    def test_find_all_lcs(self):
        self.assertEqual({"MJAU"}, find_all_lcs("XMJYAUZ", "MZJAWXU"))
        self.assertEqual({"BCAB", "BCBA", "BDAB"}, find_all_lcs("ABCBDAB", "BDCABA"))


class TestHouseRobber(unittest.TestCase):
    def test_house_robber_top_down(self):
        self.assertEqual(4, house_robber_top_down([1, 2, 3, 1]))
        self.assertEqual(12, house_robber_top_down([2, 7, 9, 3, 1]))

    def test_house_robber_bottom_up(self):
        self.assertEqual(4, house_robber_bottom_up([1, 2, 3, 1]))
        self.assertEqual(12, house_robber_bottom_up([2, 7, 9, 3, 1]))

    def test_house_robber_ii_top_down(self):
        self.assertEqual(3, house_robber_ii_top_down([2, 3, 2]))
        self.assertEqual(4, house_robber_ii_top_down([1, 2, 3, 1]))
        self.assertEqual(3, house_robber_ii_top_down([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
