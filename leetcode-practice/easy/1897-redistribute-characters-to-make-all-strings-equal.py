# LeetCode 1897. Redistribute Characters to Make All Strings Equal — Easy
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
# Submission 2197603702 — Accepted, Python3
#
# My thinking: I can move letters between the words
# freely, so what matters is the total count of each
# letter. If every letter's total count divides
# evenly by the number of words, each word can
# receive an equal share.

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        n = len(words)
        counts = {}
        for w in words:
            for ch in w:
                counts[ch] = counts.get(ch, 0) + 1
        return all(c % n == 0 for c in counts.values())
