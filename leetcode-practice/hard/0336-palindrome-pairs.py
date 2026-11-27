# LeetCode 336. Palindrome Pairs — Hard
# https://leetcode.com/problems/palindrome-pairs/
# Submission 2198407101 — Accepted, Python3
#
# My thinking: for each word I try every split into
# a front and a back. If the back is a palindrome,
# the reversed front completes a pair; if the front
# is a palindrome, the reversed back does. I look
# each reversed piece up in a map of the words. I
# skip the split at the very start for the second
# check, because it would report the same full-
# reverse pair twice.

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        index = {word: i for i, word in enumerate(words)}
        pairs = []

        def is_pal(text: str) -> bool:
            return text == text[::-1]

        for i, word in enumerate(words):
            for cut in range(len(word) + 1):
                prefix, suffix = word[:cut], word[cut:]
                if is_pal(suffix):
                    j = index.get(prefix[::-1])
                    if j is not None and j != i:
                        pairs.append([i, j])
                if cut > 0 and is_pal(prefix):
                    j = index.get(suffix[::-1])
                    if j is not None and j != i:
                        pairs.append([j, i])
        return pairs
