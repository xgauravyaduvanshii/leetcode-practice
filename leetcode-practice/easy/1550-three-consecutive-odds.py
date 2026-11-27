# LeetCode 1550. Three Consecutive Odds — Easy
# https://leetcode.com/problems/three-consecutive-odds/
# Submission 2197585506 — Accepted, Python3
#
# My thinking: I keep a running count of odd numbers
# in a row. An odd number bumps it up — if it
# reaches 3, I am done. An even number resets it
# back to zero.

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0
        for x in arr:
            if x % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
