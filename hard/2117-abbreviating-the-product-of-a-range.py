# LeetCode 2117. Abbreviating the Product of a Range — Hard
# https://leetcode.com/problems/abbreviating-the-product-of-a-range/
# Submission 2201578946 — Accepted, Python3
#
# My thinking: the middle of the product is
# far too big to write out, so I keep only
# what the answer needs — the trailing zeros
# counted off as an exponent, the last five
# digits kept exactly, and the first five read
# off the size of the number instead of the
# number itself.

import math


class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        total2 = 0
        total5 = 0
        log_sum = 0.0
        stripped = 1
        for x in range(left, right + 1):
            log_sum += math.log10(x)
            while x % 2 == 0:
                x //= 2
                total2 += 1
            while x % 5 == 0:
                x //= 5
                total5 += 1
            stripped = (stripped * x) % 100000
        zeros = min(total2, total5)
        # Y = product with the trailing zeros removed.
        suffix = stripped
        if total2 > zeros:
            suffix = (suffix * pow(2, total2 - zeros, 100000)) % 100000
        elif total5 > zeros:
            suffix = (suffix * pow(5, total5 - zeros, 100000)) % 100000
        log_y = log_sum - zeros
        digits = int(log_y) + 1
        if digits <= 10:
            # Small enough to write out exactly: recompute
            # Y without the mod, which is cheap at this size.
            exact = 1
            for x in range(left, right + 1):
                while x % 2 == 0:
                    x //= 2
                while x % 5 == 0:
                    x //= 5
                exact *= x
            if total2 > zeros:
                exact *= 2 ** (total2 - zeros)
            elif total5 > zeros:
                exact *= 5 ** (total5 - zeros)
            return f"{exact}e{zeros}"
        frac = log_y - int(log_y)
        prefix = int(10 ** (frac + 4))
        return f"{prefix}...{suffix:05d}e{zeros}"
