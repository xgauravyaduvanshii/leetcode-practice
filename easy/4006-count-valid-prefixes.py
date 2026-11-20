# 4006. Count Valid Prefixes (Easy)
# https://leetcode.com/problems/count-valid-prefixes/
# Submission 2200096132 — Accepted, Python3
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        # My thinking: a string of zeroes and ones can
        # be rearranged into an alternating string
        # exactly when the two counts differ by at
        # most one. I count the prefixes where that
        # holds.
        zeros = 0
        ones = 0
        ans = 0
        for ch in s:
            if ch == "0":
                zeros += 1
            else:
                ones += 1
            if abs(zeros - ones) <= 1:
                ans += 1
        return ans
