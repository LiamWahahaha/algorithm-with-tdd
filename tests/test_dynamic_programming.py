import unittest

from dynamic_programming.longest_common_subsequence import calculate_lcs_length_top_down, calculate_lcs_length_bottom_up


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_calculate_lcs_length(self):
        self.assertEqual(3, calculate_lcs_length_top_down("ABCDEF", "BCESA"))
        self.assertEqual(3, calculate_lcs_length_bottom_up("ABCDEF", "BCESA"))


if __name__ == '__main__':
    unittest.main()
