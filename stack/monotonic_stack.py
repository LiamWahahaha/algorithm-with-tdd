from typing import List


def find_buildings(heights: List[int]) -> List[int]:
    """
    1 <= len(heights) <= 10E4
    1 <= heights[i] <= 10E8
    """
    buildings = []

    for idx in range(len(heights) - 1, -1, -1):
        if not buildings:
            buildings.append(idx)
        else:
            if heights[idx] > heights[buildings[-1]]:
                buildings.append(idx)

    return buildings[::-1]
