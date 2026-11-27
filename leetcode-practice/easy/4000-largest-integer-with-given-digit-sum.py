# 4000. Largest Integer With Given Digit Sum (Easy)
# https://leetcode.com/problems/largest-integer-with-given-digit-sum/
# Submission 2200094786 — Accepted, Python3
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        # My thinking: the biggest digits belong at
        # the front, so I fill the number with nines
        # from the left, then the leftover, then
        # zeroes — and if even n nines cannot reach
        # the sum, there is no such number.
        if s > 9 * n:
            return -1
        digits = []
        remaining = s
        for _ in range(n):
            d = min(9, remaining)
            digits.append(d)
            remaining -= d
        return int("".join(str(d) for d in digits))
