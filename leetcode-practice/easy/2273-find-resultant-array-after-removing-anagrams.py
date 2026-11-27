# LeetCode 2273. Find Resultant Array After Removing Anagrams — Easy
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
# Submission 2197621078 — Accepted, Python3
#
# My thinking: I keep the first word, then walk
# through the rest. A word is dropped only when it
# is an anagram of the word right before it in the
# current result — I compare their sorted letters.

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        res = [words[0]]
        prev = sorted(words[0])
        for w in words[1:]:
            cur = sorted(w)
            if cur != prev:
                res.append(w)
                prev = cur
        return res
