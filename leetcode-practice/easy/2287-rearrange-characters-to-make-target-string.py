# LeetCode 2287. Rearrange Characters to Make Target String — Easy
# https://leetcode.com/problems/rearrange-characters-to-make-target-string/
# Submission 2197621659 — Accepted, Python3
#
# My thinking: I count the letters I have and the
# letters each copy of the target needs. The number
# of copies I can build is limited by the letter
# that runs out first.

from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cs = Counter(s)
        ct = Counter(target)
        return min(cs[c] // ct[c] for c in ct)
