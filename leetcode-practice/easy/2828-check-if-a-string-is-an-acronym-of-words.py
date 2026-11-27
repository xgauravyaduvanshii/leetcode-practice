# LeetCode 2828. Check if a String Is an Acronym of Words — Easy
# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/
# Submission 2198417531 — Accepted, Python3
#
# My thinking: an acronym is just the first letter
# of each word in order, so I join those letters
# together and see whether the result is exactly
# the given string.

from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(word[0] for word in words) == s
