# LeetCode 2678. Number of Senior Citizens — Easy
# https://leetcode.com/problems/number-of-senior-citizens/
# Submission 2197815270 — Accepted, Python3
#
# My thinking: each detail string stores the age as
# the two characters at positions 11 and 12. I
# count the passengers whose age is over 60.

from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for d in details if int(d[11:13]) > 60)
