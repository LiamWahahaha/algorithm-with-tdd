from functools import lru_cache


def house_robber_top_down(nums):
    """
    constraints: 1 <= nums.length <= 100
    0 <= nums[i] <= 400
    """

    @lru_cache(maxsize=None)
    def dp(idx):
        if idx < 0:
            return 0

        return max(dp(idx - 2) + nums[idx], dp(idx - 1))

    return dp(len(nums) - 1)


def house_robber_bottom_up(nums):
    if len(nums) <= 2:
        return max(nums)
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for idx in range(2, len(nums)):
        dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx])

    return dp[-1]


def house_robber_ii_top_down(nums):
    return max(house_robber_top_down(nums[:-1]), house_robber_top_down(nums[1:]))
