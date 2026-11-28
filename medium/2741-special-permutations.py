# LeetCode 2741. Special Permutations — Medium
# https://leetcode.com/problems/special-permutations/
# Submission 2205227299 — Accepted, Python3
#
# My thinking: count permutations by dynamic programming over
# subsets — dp[mask][last] is the number of ways to arrange
# exactly the elements of mask ending with last. From each
# state, extend with any unused element that divides or is
# divisible by last. The answer is the sum over all endings
# of the full mask, modulo 1e9+7.
class Solution:
    def specialPerm(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        dp = [[0] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 1
        for mask in range(1 << n):
            for last in range(n):
                if not dp[mask][last]:
                    continue
                for nxt in range(n):
                    if mask >> nxt & 1:
                        continue
                    if nums[last] % nums[nxt] == 0 or nums[nxt] % nums[last] == 0:
                        dp[mask | (1 << nxt)][nxt] = (dp[mask | (1 << nxt)][nxt] + dp[mask][last]) % MOD
        return sum(dp[(1 << n) - 1]) % MOD
