# LeetCode 1371. Find the Longest Substring Containing Vowels in Even Counts — Medium
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
# Submission 2199042343 — Accepted, Python3
#
# My thinking: five bits track whether each
# vowel has appeared an odd number of times.
# Two positions with the same pattern have an
# even count of every vowel between them.

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first = {0: -1}
        mask = 0
        best = 0
        for i, ch in enumerate(s):
            if ch in "aeiou":
                mask ^= 1 << "aeiou".index(ch)
            if mask in first:
                best = max(best, i - first[mask])
            else:
                first[mask] = i
        return best
