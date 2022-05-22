from functools import lru_cache


def calculate_lcs_length_top_down(text1, text2):
    """
    m = len(text1), n = len(text2)
    Time Complexity: O(m * n),
    Space Complexity: O(m * n),
    """

    @lru_cache(maxsize=None)
    def lcs(text1_idx, text2_idx):
        if text1_idx < 0 or text2_idx < 0:
            return 0
        if text1[text1_idx] == text2[text2_idx]:
            return lcs(text1_idx - 1, text2_idx - 1) + 1
        else:
            return max(lcs(text1_idx - 1, text2_idx), lcs(text1_idx, text2_idx - 1))

    return lcs(len(text1) - 1, len(text2) - 1)


def calculate_lcs_length_bottom_up(text1, text2):
    """
    list(enumerate(text1)) makes a copy of text1
    reversed() doesn't make a copy of the list
    """
    lookup = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    for text2_idx, char2 in reversed(list(enumerate(text2))):
        for text1_idx, char1 in reversed(list(enumerate(text1))):
            if char1 == char2:
                lookup[text1_idx][text2_idx] = lookup[text1_idx + 1][text2_idx + 1] + 1
            else:
                lookup[text1_idx][text2_idx] = max(lookup[text1_idx + 1][text2_idx], lookup[text1_idx][text2_idx + 1])

    return lookup[0][0]


def find_lcs(text1, text2):
    """
    using bottom-up to fill the lookup table and then recursively finds lcs in
    a top-down manner
    """
    lookup = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    for text2_idx in range(1, len(text2) + 1):
        for text1_idx in range(1, len(text1) + 1):
            if text1[text1_idx - 1] == text2[text2_idx - 1]:
                lookup[text1_idx][text2_idx] = lookup[text1_idx - 1][text2_idx - 1] + 1
            else:
                lookup[text1_idx][text2_idx] = max(lookup[text1_idx - 1][text2_idx], lookup[text1_idx][text2_idx - 1])

    result = []

    def lcs(text1_idx, text2_idx):
        if text1_idx == 0 or text2_idx == 0:
            return result.append("")
        if text1[text1_idx - 1] == text2[text2_idx - 1]:
            result.append(text1[text1_idx - 1])
            return lcs(text1_idx - 1, text2_idx - 1)
        elif lookup[text1_idx - 1][text2_idx] > lookup[text1_idx][text2_idx - 1]:
            return lcs(text1_idx - 1, text2_idx)
        else:
            return lcs(text1_idx, text2_idx - 1)

    lcs(len(text1), len(text2))
    return ''.join(reversed(result))


def find_all_lcs(text1, text2):
    """
    using bottom-up to fill the lookup table and then recursively finds lcs in
    a top-down manner
    """
    lookup = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    for text2_idx in range(1, len(text2) + 1):
        for text1_idx in range(1, len(text1) + 1):
            if text1[text1_idx - 1] == text2[text2_idx - 1]:
                lookup[text1_idx][text2_idx] = lookup[text1_idx - 1][text2_idx - 1] + 1
            else:
                lookup[text1_idx][text2_idx] = max(lookup[text1_idx - 1][text2_idx], lookup[text1_idx][text2_idx - 1])

    def lcs(text1_idx, text2_idx):
        if text1_idx == 0 or text2_idx == 0:
            return [""]
        if text1[text1_idx - 1] == text2[text2_idx - 1]:
            result = lcs(text1_idx - 1, text2_idx - 1)
            for idx, ith_lcs in enumerate(result):
                result[idx] = result[idx] + text1[text1_idx - 1]
            return result
        if lookup[text1_idx - 1][text2_idx] > lookup[text1_idx][text2_idx - 1]:
            return lcs(text1_idx - 1, text2_idx)
        elif lookup[text1_idx][text2_idx - 1] > lookup[text1_idx - 1][text2_idx]:
            return lcs(text1_idx, text2_idx - 1)
        else:
            return lcs(text1_idx - 1, text2_idx) + lcs(text1_idx, text2_idx - 1)

    return set(lcs(len(text1), len(text2)))
