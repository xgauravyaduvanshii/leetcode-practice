# 3950. Exactly One Consecutive Set Bits Pair (Easy)
# https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/
# Submission 2200090968 — Accepted, Python3
class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        # My thinking: write the number in binary and
        # count the places where two ones sit side by
        # side. The answer is yes only when there is
        # exactly one such place.
        b = bin(n)[2:]
        return sum(1 for i in range(len(b) - 1) if b[i] == "1" and b[i + 1] == "1") == 1
