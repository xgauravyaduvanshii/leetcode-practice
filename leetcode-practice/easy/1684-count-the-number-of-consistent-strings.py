# LeetCode 1684. Count the Number of Consistent Strings — Easy
# https://leetcode.com/problems/count-the-number-of-consistent-strings/
# Submission 2197593491 — Accepted, Python3
#
# My thinking: a word is consistent if every one of
# its letters is in the allowed set. I turn the
# allowed letters into a set for quick lookups and
# count the words that pass the check.

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0
        for word in words:
            if all(ch in allowed_set for ch in word):
                count += 1
        return count
