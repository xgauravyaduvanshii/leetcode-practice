from functools import lru_cache


class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        # My thinking: split the pile in two — keep the
        # smaller side's sum and play on with it, or take the
        # better side when both weigh the same.
        n = len(stoneValue)
        prefix = [0]
        for v in stoneValue:
            prefix.append(prefix[-1] + v)

        def total(l, r):
            return prefix[r + 1] - prefix[l]

        @lru_cache(maxsize=None)
        def dp(l, r):
            if l == r:
                return 0
            best = 0
            for k in range(l, r):
                left = total(l, k)
                right = total(k + 1, r)
                if left < right:
                    best = max(best, left + dp(l, k))
                elif left > right:
                    best = max(best, right + dp(k + 1, r))
                else:
                    best = max(best, left + dp(l, k), right + dp(k + 1, r))
            return best

        return dp(0, n - 1)
