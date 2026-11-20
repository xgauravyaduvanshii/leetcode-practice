from functools import lru_cache


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        # My thinking: write the target in base x — each digit d
        # costs d copies of x^i, or x - d copies going the other
        # way with a carry to the next digit. Fewest copies of x
        # means fewest operators, since operators = copies - 1.
        digits = []
        t = target
        while t:
            digits.append(t % x)
            t //= x

        @lru_cache(maxsize=None)
        def dp(pos, carry):
            if pos == len(digits):
                return carry * pos
            d = digits[pos] + carry
            unit = pos if pos >= 1 else 2
            best = dp(pos + 1, 0) + d * unit
            if d > 0:
                best = min(best, dp(pos + 1, 1) + (x - d) * unit)
            return best

        return dp(0, 0) - 1
