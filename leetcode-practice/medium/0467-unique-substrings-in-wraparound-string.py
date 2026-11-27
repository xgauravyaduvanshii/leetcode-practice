# LeetCode 467. Unique Substrings in Wraparound String — Medium
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/
# Submission 2198809724 — Accepted, Python3
#
# My thinking: every wraparound substring ends at
# some letter, and the longest run ending at that
# letter covers all the shorter ones. I track the
# longest valid run ending at each letter and add
# those lengths up.

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        longest = {}
        run = 0
        for i, char in enumerate(s):
            if i > 0 and (ord(char) - ord(s[i - 1])) % 26 == 1:
                run += 1
            else:
                run = 1
            longest[char] = max(longest.get(char, 0), run)
        return sum(longest.values())
