from functools import lru_cache


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        # My thinking: count the numbers with all different digits
        # and subtract from n — a digit DP over the used-digit mask
        # does the counting.
        digits = list(map(int, str(n)))

        @lru_cache(maxsize=None)
        def count(pos, mask, tight, started):
            if pos == len(digits):
                return 1 if started else 0
            limit = digits[pos] if tight else 9
            total = 0
            for d in range(limit + 1):
                new_tight = tight and d == limit
                if not started and d == 0:
                    total += count(pos + 1, mask, new_tight, False)
                elif mask & (1 << d):
                    continue
                else:
                    total += count(pos + 1, mask | (1 << d), new_tight, True)
            return total

        return n - count(0, 0, True, False)
