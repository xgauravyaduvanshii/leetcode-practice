# LeetCode 1758. Minimum Changes To Make Alternating Binary String — Easy
# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
# Submission 2197597216 — Accepted, Python3
#
# My thinking: there are only two alternating
# patterns — starting with 0 or starting with 1.
# I count how many flips the first pattern needs;
# the second pattern needs the rest of the
# positions, so the answer is the smaller of the
# two.

class Solution:
    def minOperations(self, s: str) -> int:
        mismatches = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                mismatches += 1
        return min(mismatches, len(s) - mismatches)
