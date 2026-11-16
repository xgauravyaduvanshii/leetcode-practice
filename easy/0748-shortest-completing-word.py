# LeetCode 748. Shortest Completing Word — Easy
# https://leetcode.com/problems/shortest-completing-word/
# Submission 2197525458 — Accepted, Python3
#
# My thinking: first I count the letters the license
# plate needs (letters only, ignoring case and
# digits). Then I check each word — it has to
# contain at least that many of every needed
# letter — and I keep the shortest one that does.

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        needed = {}
        for ch in licensePlate.lower():
            if ch.isalpha():
                needed[ch] = needed.get(ch, 0) + 1
        best = None
        for word in words:
            counts = {}
            for ch in word:
                counts[ch] = counts.get(ch, 0) + 1
            if all(counts.get(ch, 0) >= n for ch, n in needed.items()):
                if best is None or len(word) < len(best):
                    best = word
        return best
