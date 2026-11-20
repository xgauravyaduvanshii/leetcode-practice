# LeetCode 1641. Count Sorted Vowel Strings — Medium
# https://leetcode.com/problems/count-sorted-vowel-strings/
# Submission 2199899946 — Accepted, Python3
#
# My thinking: a string ending in a vowel can
# only continue with that vowel or a later
# one. I keep five running counts, one per
# last vowel, and grow them one letter at a
# time.

class Solution:
    def countVowelStrings(self, n: int) -> int:
        counts = [1] * 5
        for _ in range(1, n):
            for i in range(1, 5):
                counts[i] += counts[i - 1]
        return sum(counts)
