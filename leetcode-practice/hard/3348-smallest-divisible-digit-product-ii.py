# LeetCode 3348. Smallest Divisible Digit Product II — Hard
# https://leetcode.com/problems/smallest-divisible-digit-product-ii/
# Submission 2202407607 — Accepted, Python3
from functools import lru_cache


class Solution:
    def smallestDivisibleDigitProduct(self, num: str, t: int) -> str:
        # My thinking: a digit product only involves the primes 2, 3, 5, 7,
        # so if t has any other prime factor the answer is -1. Otherwise I
        # factor t into the exponents it needs, and a memoised DP gives the
        # fewest digits covering any remaining exponents. For the same length
        # I keep the longest possible prefix of num and raise the rightmost
        # digit I can, filling the rest with the smallest feasible digits.
        # If that fails I use a longer length, where the fewest digits
        # (lexicographically smallest, padded with 1s) is optimal — more 1s
        # up front always beats any other multiset of the same length.
        need = [0, 0, 0, 0]  # exponents of 2, 3, 5, 7
        x = t
        for i, p in enumerate((2, 3, 5, 7)):
            while x % p == 0:
                need[i] += 1
                x //= p
        if x != 1:
            return "-1"
        need = tuple(need)
        contrib = {
            2: (1, 0, 0, 0), 3: (0, 1, 0, 0), 4: (2, 0, 0, 0),
            5: (0, 0, 1, 0), 6: (1, 1, 0, 0), 7: (0, 0, 0, 1),
            8: (3, 0, 0, 0), 9: (0, 2, 0, 0),
        }

        @lru_cache(maxsize=None)
        def min_digits(a, b, c, d):
            if a == 0 and b == 0 and c == 0 and d == 0:
                return 0
            best = 10 ** 9
            for da, db, dc, dd in contrib.values():
                # a digit that covers nothing still needed is useless here
                # (and would recurse on the same state forever)
                if not ((da and a) or (db and b) or (dc and c) or (dd and d)):
                    continue
                best = min(best, 1 + min_digits(max(0, a - da), max(0, b - db),
                                                max(0, c - dc), max(0, d - dd)))
            return best

        def sub(state, digit):
            if digit == 1:
                return state
            da, db, dc, dd = contrib[digit]
            a, b, c, d = state
            return (max(0, a - da), max(0, b - db),
                    max(0, c - dc), max(0, d - dd))

        n = len(num)
        digits = [ord(ch) - 48 for ch in num]
        # prefix exponent sums (clipped at need) and prefix zero counts
        pref = [(0, 0, 0, 0)]
        pref_zero = [0]
        for dg in digits:
            a, b, c, d = pref[-1]
            if dg >= 2:
                da, db, dc, dd = contrib[dg]
                a = min(need[0], a + da)
                b = min(need[1], b + db)
                c = min(need[2], c + dc)
                d = min(need[3], d + dd)
            pref.append((a, b, c, d))
            pref_zero.append(pref_zero[-1] + (1 if dg == 0 else 0))
        if pref_zero[n] == 0 and pref[n] == need:
            return num
        # same-length search: split at i, rightmost first
        for i in range(n - 1, -1, -1):
            if pref_zero[i] != 0:
                continue
            for d in range(digits[i] + 1, 10):
                rem = sub(tuple(need[j] - pref[i][j] for j in range(4)), d)
                r = n - 1 - i
                if min_digits(*rem) > r:
                    continue
                out = digits[:i] + [d]
                state = rem
                for pos in range(i + 1, n):
                    left = n - 1 - pos
                    for dd in range(1, 10):
                        ns = sub(state, dd)
                        if min_digits(*ns) <= left:
                            out.append(dd)
                            state = ns
                            break
                return ''.join(str(v) for v in out)
        # longer length: fewest digits, lexicographically smallest
        m = min_digits(*need)
        state = need
        chosen = []
        prev = 2
        while state != (0, 0, 0, 0):
            cur = min_digits(*state)
            for d in range(prev, 10):
                ns = sub(state, d)
                if min_digits(*ns) == cur - 1:
                    chosen.append(d)
                    state = ns
                    prev = d
                    break
        length = max(n + 1, m)
        ans_digits = [1] * (length - len(chosen)) + chosen
        return ''.join(str(v) for v in ans_digits)
