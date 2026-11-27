from functools import lru_cache


class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        # My thinking: the first cut splits the stick in two
        # and costs the whole length — so try every cut first
        # and add the best bills of the two pieces.
        cuts = sorted([0] + cuts + [n])

        @lru_cache(maxsize=None)
        def dp(i, j):
            if j - i <= 1:
                return 0
            return cuts[j] - cuts[i] + min(dp(i, k) + dp(k, j) for k in range(i + 1, j))

        return dp(0, len(cuts) - 1)
