# LeetCode 2145. Count the Hidden Sequences — Medium
# https://leetcode.com/problems/count-the-hidden-sequences/
# Submission 2204473925 — Accepted, Python3
#
# My thinking: the differences fix the shape of the hidden array up to
# its starting value, so I track the running prefix sums and their
# minimum and maximum. The start can shift only while the whole shifted
# array stays inside [lower, upper], which gives a range of valid starts
# whose size is the answer — or zero if the range is empty.
class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        pref = 0
        mn = 0
        mx = 0
        for d in differences:
            pref += d
            if pref < mn:
                mn = pref
            if pref > mx:
                mx = pref
        lo = lower - mn
        hi = upper - mx
        return hi - lo + 1 if hi >= lo else 0
