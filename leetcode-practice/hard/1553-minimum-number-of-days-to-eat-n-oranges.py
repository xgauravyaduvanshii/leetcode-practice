from functools import lru_cache


class Solution:
    def minDays(self, n: int) -> int:
        # My thinking: the big bites need a divisible pile,
        # so eat single oranges just until the pile divides
        # by two or by three, then take the big bite.
        @lru_cache(maxsize=None)
        def dp(x):
            if x <= 1:
                return x
            return 1 + min(x % 2 + dp(x // 2), x % 3 + dp(x // 3))

        return dp(n)
