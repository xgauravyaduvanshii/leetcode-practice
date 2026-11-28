# LeetCode 2559. Count Vowel Strings in Ranges — Medium
# https://leetcode.com/problems/count-vowel-strings-in-ranges/
# Submission 2205067204 — Accepted, Python3
#
# My thinking: a word counts when its first and last letters are
# both vowels. A prefix sum over that 0/1 flag answers each
# query in O(1).
class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = set("aeiou")
        pref = [0]
        for w in words:
            pref.append(pref[-1] + (w[0] in vowels and w[-1] in vowels))
        return [pref[r + 1] - pref[l] for l, r in queries]
