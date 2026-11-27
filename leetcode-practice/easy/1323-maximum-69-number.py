# LeetCode 1323. Maximum 69 Number — Easy
# https://leetcode.com/problems/maximum-69-number/
# Submission 2197570789 — Accepted, Python3
#
# My thinking: changing a 6 to a 9 always makes the
# number bigger, and the earlier the change, the
# bigger the gain. So I change the first 6 I find
# and leave everything else alone.

class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))
