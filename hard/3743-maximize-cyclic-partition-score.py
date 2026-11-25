# LeetCode 3743. Maximize Cyclic Partition Score — Hard
# https://leetcode.com/problems/maximize-cyclic-partition-score/
# Submission 2203147220 — Accepted, Python3
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # My thinking: a segment scores its max minus its min,
        # so the whole partition scores the sum of the picked
        # maxes minus the sum of the picked mins. I walk the
        # array once and pick some elements as a segment max
        # (+x) or a segment min (-x), skipping the rest. The
        # two picks of one segment sit side by side in the
        # cyclic order, so the running difference between max
        # picks and min picks only ever takes the values -1, 0
        # and 1 — I keep it as a balance of 0, 1 or 2. Because
        # the array is cyclic, the cut between the last and the
        # first element can fall inside a pair, so the balance
        # at the start of the scan can be 0, 1 or 2; I try all
        # three and require the balance to return to its
        # starting value at the end, which also forces the
        # numbers of max and min picks to match. The count c
        # of max picks is the number of segments used, capped
        # at k, and skipping a bad pair is always free, so the
        # best score over the three starts is the answer.
        NEG = -10 ** 18
        best = 0
        for b0 in (0, 1, 2):
            dp = [[NEG] * 3 for _ in range(k + 1)]
            dp[0][b0] = 0
            for i, x in enumerate(nums):
                ndp = [row[:] for row in dp]
                for c in range(min(k, i) + 1):
                    for b in range(3):
                        v = dp[c][b]
                        if v == NEG:
                            continue
                        if b < 2 and c < k and v + x > ndp[c + 1][b + 1]:
                            ndp[c + 1][b + 1] = v + x
                        if b > 0 and v - x > ndp[c][b - 1]:
                            ndp[c][b - 1] = v - x
                dp = ndp
            for c in range(k + 1):
                if dp[c][b0] > best:
                    best = dp[c][b0]
        return best
