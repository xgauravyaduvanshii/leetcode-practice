# 3184. Count Pairs That Form a Complete Day I (Easy)
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/
# Submission 2199984126 — Accepted, Python3
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # My thinking: two hours make a full day when
        # their remainders after dividing by 24 add up
        # to 24 (or both are already 0). I count the
        # remainders, then pair each remainder with the
        # one that completes it.
        remainders = {}
        count = 0
        for h in hours:
            r = h % 24
            need = (24 - r) % 24
            count += remainders.get(need, 0)
            remainders[r] = remainders.get(r, 0) + 1
        return count
