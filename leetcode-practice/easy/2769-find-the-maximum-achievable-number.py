# LeetCode 2769. Find the Maximum Achievable Number — Easy
# https://leetcode.com/problems/find-the-maximum-achievable-number/
# Submission 2198361221 — Accepted, Python3
#
# My thinking: every operation lets me push the
# number up by one while the counter drops by
# one — and the same operation also lets me pull
# the number the other way. The best I can do is
# spend all t operations going up, which gains
# two per operation on top of the starting number.

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t
