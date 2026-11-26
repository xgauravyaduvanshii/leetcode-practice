# LeetCode 3869. Count Fancy Numbers in a Range — Hard
# https://leetcode.com/problems/count-fancy-numbers-in-a-range/
# Submission 2203328363 — Accepted, Python3
from functools import lru_cache


def _is_good_number(x: int) -> bool:
    # True when the decimal digits of x are strictly
    # monotone; a single digit is good by definition.
    ds = [int(c) for c in str(x)]
    if len(ds) <= 1:
        return True
    inc = all(ds[i] < ds[i + 1] for i in range(len(ds) - 1))
    dec = all(ds[i] > ds[i + 1] for i in range(len(ds) - 1))
    return inc or dec


class Solution:
    def countFancy(self, l: int, r: int) -> int:
        # My thinking: count fancy numbers up to n with a
        # digit DP, then answer F(r) - F(l - 1). The DP walks
        # the decimal digits of n tracking tight, whether a
        # digit has started, the last digit placed, the
        # direction of the digits so far (undecided,
        # increasing, decreasing, or already broken) and the
        # digit sum, which is at most 9 * 16 = 144. At the
        # end a number is fancy when its digits stayed
        # strictly monotone, or when its digit sum — itself
        # a one-to-three-digit number — is good. Leading
        # zeros never start the number, so 0 is not counted.
        def count_upto(n: int) -> int:
            if n <= 0:
                return 0
            digits = [int(c) for c in str(n)]

            @lru_cache(maxsize=None)
            def dfs(pos, tight, started, last, direction, digit_sum):
                if pos == len(digits):
                    if not started:
                        return 0
                    if direction != 3:
                        return 1
                    return 1 if _is_good_number(digit_sum) else 0
                limit = digits[pos] if tight else 9
                res = 0
                for d in range(limit + 1):
                    ntight = tight and d == limit
                    if not started and d == 0:
                        res += dfs(pos + 1, ntight, False, 0, 0, digit_sum)
                    else:
                        if not started:
                            ndirection = 0
                        elif direction == 3:
                            ndirection = 3
                        elif direction == 0:
                            ndirection = 1 if d > last else (2 if d < last else 3)
                        elif direction == 1:
                            ndirection = 1 if d > last else 3
                        else:
                            ndirection = 2 if d < last else 3
                        res += dfs(pos + 1, ntight, True, d, ndirection, digit_sum + d)
                return res

            return dfs(0, True, False, 0, 0, 0)

        return count_upto(r) - count_upto(l - 1)
