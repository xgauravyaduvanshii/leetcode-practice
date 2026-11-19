# LeetCode 1227. Airplane Seat Assignment Probability — Medium
# https://leetcode.com/problems/airplane-seat-assignment-probability/
# Submission 2199013808 — Accepted, Python3
#
# My thinking: the first passenger either takes
# their own seat — then everyone sits as
# planned — or takes the last seat, and then the
# last passenger misses theirs. Those two
# chances are equal.

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5
