# LeetCode 2551. Put Marbles in Bags — Hard
# https://leetcode.com/problems/put-marbles-in-bags/
# Submission 2201810215 — Accepted, Python3
#
# My thinking: every split between two
# bags adds the pair of marbles it
# touches, so the whole score is the
# first and last marble plus the pairs
# at the cuts — the dearest cuts and the
# cheapest cuts give the two extremes,
# and their gap is the answer.

class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        n = len(weights)
        if k == 1 or n == k:
            return 0
        pairs = sorted(weights[i] + weights[i + 1] for i in range(n - 1))
        return sum(pairs[-(k - 1):]) - sum(pairs[:k - 1])
