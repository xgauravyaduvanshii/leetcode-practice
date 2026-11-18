# LeetCode 3014. Minimum Number of Pushes to Type Word I — Easy
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/
# Submission 2198715472 — Accepted, Python3
#
# My thinking: every key holds up to 8 letters, the
# first 8 letters cost one push each, the next 8 cost
# two, and so on. The letters are all distinct here,
# so I just add one push per letter for the first
# eight, two for the next eight, and keep counting.

class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        for position, _ in enumerate(word):
            pushes += position // 8 + 1
        return pushes
