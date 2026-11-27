# LeetCode 2586. Count the Number of Vowel Strings in Range — Easy
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/
# Submission 2197806891 — Accepted, Python3
#
# My thinking: I check only the words from left to
# right in the range and count the ones that start
# and end with a vowel.

class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = set('aeiou')
        count = 0
        for i in range(left, right + 1):
            w = words[i]
            if w[0] in vowels and w[-1] in vowels:
                count += 1
        return count
