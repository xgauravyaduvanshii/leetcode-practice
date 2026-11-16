# LeetCode 696. Count Binary Substrings — Easy
# https://leetcode.com/problems/count-binary-substrings/
# Submission 2197515915 — Accepted, Python3
#
# My thinking: I group the string into runs of the
# same digit — say 3 zeros then 2 ones. Any valid
# substring sits across two neighbouring runs, and
# there are as many of them as the shorter of the
# two runs. So I add up the smaller of each pair
# of neighbouring run lengths.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)
        return sum(min(groups[i], groups[i + 1]) for i in range(len(groups) - 1))
