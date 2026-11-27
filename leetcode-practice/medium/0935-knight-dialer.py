# LeetCode 935. Knight Dialer — Medium
# https://leetcode.com/problems/knight-dialer/
# Submission 2198972808 — Accepted, Python3
#
# My thinking: I count how many ways the knight
# can end on each digit after each press. Every
# step, each digit hands its count to the digits
# a knight can jump to from it.

class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        moves = {
            0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8),
            4: (0, 3, 9), 5: (), 6: (0, 1, 7),
            7: (2, 6), 8: (1, 3), 9: (2, 4),
        }
        counts = [1] * 10
        for _ in range(n - 1):
            new_counts = [0] * 10
            for digit in range(10):
                for nxt in moves[digit]:
                    new_counts[nxt] = (new_counts[nxt] + counts[digit]) % MOD
            counts = new_counts
        return sum(counts) % MOD
