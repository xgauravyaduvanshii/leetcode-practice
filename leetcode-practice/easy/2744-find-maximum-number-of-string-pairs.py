# LeetCode 2744. Find Maximum Number of String Pairs — Easy
# https://leetcode.com/problems/find-maximum-number-of-string-pairs/
# Submission 2198358209 — Accepted, Python3
#
# My thinking: two words pair up when one is the
# reverse of the other. I walk through the words
# once, keeping the ones I have seen. When a word's
# reverse is already waiting there, that makes a
# pair, and I take the reverse out so no word is
# used twice.

from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        pairs = 0
        for word in words:
            if word[::-1] in seen:
                pairs += 1
                seen.remove(word[::-1])
            else:
                seen.add(word)
        return pairs
