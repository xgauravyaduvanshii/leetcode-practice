# LeetCode 2745. Construct the Longest New String — Medium
# https://leetcode.com/problems/construct-the-longest-new-string/
# Submission 2205232261 — Accepted, Python3
#
# My thinking: "AA" and "BB" blocks must alternate (two of a
# kind in a row would make "AAA" or "BBB"), so they contribute
# 2*min(x, y) blocks, plus one extra block of the majority
# kind when x != y. All z "AB" blocks can be used together at
# one end, where "ABAB..." never forms a triple. Each block is
# 2 letters, so the length is twice the block count. (An
# earlier DP over block counts timed out; this closed form
# replaces it.)
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return 2 * (2 * min(x, y) + z + (1 if x != y else 0))
