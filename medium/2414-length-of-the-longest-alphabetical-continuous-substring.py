# LeetCode 2414. Length of the Longest Alphabetical Continuous Substring — Medium
# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
# Submission 2204793856 — Accepted, Python3
#
# My thinking: one pass tracks the current run of consecutive letters
# (each character exactly one more than the previous). A break resets
# the run to 1; the longest run seen is the answer.
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        cur = 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                cur += 1
            else:
                cur = 1
            ans = max(ans, cur)
        return ans
