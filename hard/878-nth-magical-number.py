import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # My thinking: the magical numbers thin out evenly, so count
        # how many sit below a guess and binary-search the smallest
        # guess holding n of them.
        MOD = 10 ** 9 + 7
        lcm = a * b // math.gcd(a, b)

        def count(x):
            return x // a + x // b - x // lcm

        lo, hi = 1, n * min(a, b)
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) < n:
                lo = mid + 1
            else:
                hi = mid
        return lo % MOD
