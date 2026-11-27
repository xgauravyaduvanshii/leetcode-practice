# 744. Find Smallest Letter Greater Than Target (Easy)
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Submission 2199964010 — Accepted, Python3
from bisect import bisect_right
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # My thinking: the letters are sorted, so the
        # answer is the first one after the target. If
        # nothing is bigger, the list wraps around to
        # its first letter.
        i = bisect_right(letters, target)
        return letters[i % len(letters)]
