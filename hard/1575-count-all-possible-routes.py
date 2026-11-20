from functools import lru_cache


class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        # My thinking: from any city with fuel left you may
        # stop at the finish or drive on — so count the stop
        # plus every onward trip you can still afford.
        MOD = 10 ** 9 + 7

        @lru_cache(maxsize=None)
        def dp(pos, left):
            total = 1 if pos == finish else 0
            for nxt in range(len(locations)):
                if nxt == pos:
                    continue
                cost = abs(locations[pos] - locations[nxt])
                if cost <= left:
                    total = (total + dp(nxt, left - cost)) % MOD
            return total

        return dp(start, fuel)
