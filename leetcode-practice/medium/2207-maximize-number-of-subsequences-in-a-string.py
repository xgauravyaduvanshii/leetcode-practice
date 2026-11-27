# LeetCode 2207. Maximize Number of Subsequences in a String — Medium
# https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/
# Submission 2204499061 — Accepted, Python3
#
# My thinking: inserting one letter can only help at the ends, so the
# best insert is either a copy of pattern[0] at the front or a copy of
# pattern[1] at the back. I count the existing pairs in one pass, then
# add whichever insert helps more: the number of pattern[0] letters for
# a front insert, or the number of pattern[1] letters for a back insert.
# When both pattern letters are the same, one insert adds exactly the
# current count of that letter as new pairs.
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        a, b = pattern[0], pattern[1]
        if a == b:
            cnt = text.count(a)
            return cnt * (cnt + 1) // 2
        pairs = 0
        seen_a = 0
        cnt_a = 0
        cnt_b = 0
        for ch in text:
            if ch == a:
                seen_a += 1
                cnt_a += 1
            elif ch == b:
                cnt_b += 1
                pairs += seen_a
        return pairs + max(cnt_a, cnt_b)
