# LeetCode 2400. Number of Ways to Reach a Position After Exactly k Steps — Medium
# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
# Submission 2204782434 — Accepted, Python3
#
# My thinking: to end at distance d after k steps, the walk must take
# (k + d) / 2 steps in the direction of the target and the rest the
# other way — so the answer is C(k, right). Impossible when the target
# is farther than k steps or the parity doesn't match (each extra pair
# of steps is a wasted back-and-forth).
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        import math
        d = endPos - startPos
        if abs(d) > k or (k - abs(d)) % 2 == 1:
            return 0
        right = (k + d) // 2
        return math.comb(k, right) % 1000000007
