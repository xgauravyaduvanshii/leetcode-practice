# 3783. Mirror Distance of an Integer (Easy)
# https://leetcode.com/problems/mirror-distance-of-an-integer/
# Submission 2200065116 — Accepted, Python3
class Solution:
    def mirrorDistance(self, n: int) -> int:
        # My thinking: flip the digits around and see
        # how far the flipped number sits from the
        # original.
        return abs(n - int(str(n)[::-1]))
