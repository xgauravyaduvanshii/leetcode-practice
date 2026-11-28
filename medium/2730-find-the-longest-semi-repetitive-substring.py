# LeetCode 2730. Find the Longest Semi-Repetitive Substring — Medium
# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/
# Submission 2205212655 — Accepted, Python3
#
# My thinking: slide a window over the string, counting how
# many adjacent equal pairs it holds. With at most one such
# pair allowed, shrink the window from the left whenever a
# second pair enters; the longest window seen is the answer.
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        left = 0
        pairs = 0
        for right in range(1, n):
            if s[right] == s[right - 1]:
                pairs += 1
            while pairs > 1:
                if s[left] == s[left + 1]:
                    pairs -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
