# LeetCode 343. Integer Break — Medium
# https://leetcode.com/problems/integer-break/
# Submission 2198755342 — Accepted, Python3
#
# My thinking: threes multiply best, so I keep
# peeling off 3s until 4 or less is left, then
# multiply in the remainder. Small numbers are the
# exception — splitting 2 or 3 once beats leaving
# them whole.

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        product = 1
        while n > 4:
            product *= 3
            n -= 3
        return product * n
