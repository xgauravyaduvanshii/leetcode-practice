# LeetCode 819. Most Common Word — Easy
# https://leetcode.com/problems/most-common-word/
# Submission 2197531351 — Accepted, Python3
#
# My thinking: I read the paragraph one character at
# a time, building up words from letters and
# splitting on anything that is not a letter. I
# count each word that is not banned, and at the
# end the most frequent one wins.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)
        counts = {}
        word = []
        for ch in paragraph.lower():
            if ch.isalpha():
                word.append(ch)
            else:
                if word:
                    w = "".join(word)
                    if w not in banned_set:
                        counts[w] = counts.get(w, 0) + 1
                    word = []
        if word:
            w = "".join(word)
            if w not in banned_set:
                counts[w] = counts.get(w, 0) + 1
        return max(counts, key=counts.get)
