# LeetCode 1790. Check if One String Swap Can Make Strings Equal — Easy
# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
# Submission 2197598055 — Accepted, Python3
#
# My thinking: I collect the positions where the two
# strings differ. If there are none, they are
# already equal. If there are exactly two, swapping
# those two characters in one string has to fix
# both — so I check that they match cross-wise.
# Any other count cannot be fixed with one swap.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if not diffs:
            return True
        if len(diffs) != 2:
            return False
        i, j = diffs
        return s1[i] == s2[j] and s1[j] == s2[i]
