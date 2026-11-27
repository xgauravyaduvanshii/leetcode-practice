# LeetCode 2262. Total Appeal of A String — Hard
# https://leetcode.com/problems/total-appeal-of-a-string/
# Submission 2201641865 — Accepted, Python3
#
# My thinking: a letter only adds to the
# substrings ending here when it has not
# shown up since the substring began — so
# each position adds exactly the gap back
# to its last sighting.

class Solution:
    def appealSum(self, s: str) -> int:
        last = {}
        dp = 0
        total = 0
        for i, c in enumerate(s):
            prev = last.get(c, -1)
            dp += i - prev
            total += dp
            last[c] = i
        return total
