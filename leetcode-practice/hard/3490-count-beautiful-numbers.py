# LeetCode 3490. Count Beautiful Numbers — Hard
# https://leetcode.com/problems/count-beautiful-numbers/
# Submission 2202710448 — Accepted, Python3

from functools import lru_cache


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        # My thinking: a number is beautiful when its digit product
        # is a multiple of its digit sum. A zero digit makes the
        # product 0, which is a multiple of any sum, so those numbers
        # are all beautiful. I count numbers up to X by fixing the
        # digit sum s (at most 9 * 9 = 81) and running a digit DP
        # that tracks the product modulo s and the running sum.
        # The digit is always added to the sum, even after the
        # product has become 0 — skipping that update was the bug
        # in my first attempt, it undercounted the sum for numbers
        # like 101. The answer is count(r) - count(l - 1).
        def count(X):
            if X <= 0:
                return 0
            digits = str(X)
            n = len(digits)
            total = 0
            for target in range(1, 9 * n + 1):
                @lru_cache(maxsize=None)
                def dp(pos, prod_mod, sum_so_far, tight, started):
                    if pos == n:
                        return 1 if (started and sum_so_far == target and prod_mod == 0) else 0
                    limit = int(digits[pos]) if tight else 9
                    ans = 0
                    for dgt in range(limit + 1):
                        ntight = tight and (dgt == limit)
                        if not started and dgt == 0:
                            ans += dp(pos + 1, prod_mod, sum_so_far, ntight, False)
                        else:
                            nsum = sum_so_far + dgt
                            if nsum > target:
                                continue
                            nprod = (dgt % target) if not started else (prod_mod * dgt) % target
                            ans += dp(pos + 1, nprod, nsum, ntight, True)
                    return ans
                total += dp(0, 0, 0, True, False)
            return total

        return count(r) - count(l - 1)
