# LeetCode 242. Valid Anagram — Easy
# https://leetcode.com/problems/valid-anagram/
# Submission 2197457182 — Accepted, Python3
#
# My thinking: two words are anagrams if they have
# exactly the same letters. Sorting both puts those
# letters in the same order, so if the sorted
# versions match, the words are anagrams.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
