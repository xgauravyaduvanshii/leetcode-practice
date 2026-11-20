from functools import lru_cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        # My thinking: walk the string left to right, staying
        # between the two bounds and tracking how much of the
        # forbidden word we have matched so far — the prefix
        # function tells us where to fall back when a letter
        # breaks the match.
        MOD = 10 ** 9 + 7
        m = len(evil)
        pi = [0] * m
        for i in range(1, m):
            j = pi[i - 1]
            while j > 0 and evil[i] != evil[j]:
                j = pi[j - 1]
            if evil[i] == evil[j]:
                j += 1
            pi[i] = j

        def nxt(state, ch):
            while state > 0 and evil[state] != ch:
                state = pi[state - 1]
            if evil[state] == ch:
                state += 1
            return state

        @lru_cache(maxsize=None)
        def dp(pos, low_tight, high_tight, state):
            if state == m:
                return 0
            if pos == n:
                return 1
            total = 0
            lo = ord(s1[pos]) if low_tight else ord("a")
            hi = ord(s2[pos]) if high_tight else ord("z")
            for code in range(lo, hi + 1):
                ch = chr(code)
                total = (total + dp(pos + 1,
                                    low_tight and code == ord(s1[pos]),
                                    high_tight and code == ord(s2[pos]),
                                    nxt(state, ch))) % MOD
            return total

        return dp(0, True, True, 0)
