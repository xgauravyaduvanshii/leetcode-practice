# LeetCode 1247. Minimum Swaps to Make Strings Equal — Medium
# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
# Submission 2199017818 — Accepted, Python3
#
# My thinking: only the mismatched spots matter
# — x-over-y and y-over-x. Two of the same kind
# fix with one swap, and one of each kind needs
# two swaps. An odd total can never be fixed.

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == "x" and b == "y":
                xy += 1
            elif a == "y" and b == "x":
                yx += 1
        if (xy + yx) % 2 == 1:
            return -1
        return xy // 2 + yx // 2 + (xy % 2) * 2
