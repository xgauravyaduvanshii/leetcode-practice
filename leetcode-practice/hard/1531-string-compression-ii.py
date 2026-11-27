from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # My thinking: delete up to k letters, then the cost
        # of each run is 1 plus the digits of its length — so
        # remember the last letter and how long its run is.
        n = len(s)

        def digits(c):
            if c == 1:
                return 0
            if c < 10:
                return 1
            if c < 100:
                return 2
            return 3

        @lru_cache(maxsize=None)
        def dp(i, left, last, count):
            if left < 0:
                return float("inf")
            if i == n:
                return 0
            best = dp(i + 1, left - 1, last, count)
            if s[i] == last:
                best = min(best, dp(i + 1, left, last, count + 1) + digits(count + 1) - digits(count))
            else:
                best = min(best, dp(i + 1, left, s[i], 1) + 1)
            return best

        return dp(0, k, "", 0)
