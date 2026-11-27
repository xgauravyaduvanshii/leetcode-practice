# LeetCode 3666. Minimum Operations to Equalize Binary String — Hard
# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/
# Submission 2203022531 — Accepted, Python3


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # My thinking: with t operations I flip t * k bits in total.
        # Every '0' must be flipped an odd number of times and every
        # '1' an even number of times, so t * k must have the same
        # parity as the number of zeroes, and the zeroes need at
        # least one flip each. A single position can only be flipped
        # once per operation, so the zeroes can absorb at most
        # z * t flips when t is odd (z * (t - 1) when t is even,
        # since an odd count can never reach t), and the same cap
        # holds for the ones; each operation also has to flip at
        # least k - (n - z) zeroes because there are only that many
        # ones to fill the rest. I try t = 1, 2, 3, ... and take the
        # first t where some flip count a for the zeroes fits all
        # of those bounds with the right parity — that t is minimal,
        # and if no t fits the string can never become all '1's.
        n = len(s)
        z = s.count('0')
        if z == 0:
            return 0
        for t in range(1, 10 ** 6 + 1):
            if (t * k - z) % 2 != 0:
                continue
            ones_cap = (n - z) * (t if t % 2 == 0 else t - 1)
            zero_cap = z * (t if t % 2 == 1 else t - 1)
            lo = max(z, t * max(0, k - (n - z)), t * k - ones_cap)
            hi = min(t * min(k, z), zero_cap)
            if lo > hi:
                continue
            a = lo if lo % 2 == z % 2 else lo + 1
            if a <= hi:
                return t
        return -1
