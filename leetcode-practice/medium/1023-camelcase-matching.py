# LeetCode 1023. Camelcase Matching — Medium
# https://leetcode.com/problems/camelcase-matching/
# Submission 2198988740 — Accepted, Python3
#
# My thinking: I scan each query looking for the
# pattern letters in order. A lowercase letter
# that is not in the pattern can be skipped, but
# an extra uppercase letter breaks the match.

from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def matches(query):
            i = 0
            for ch in query:
                if i < len(pattern) and ch == pattern[i]:
                    i += 1
                elif ch.isupper():
                    return False
            return i == len(pattern)

        return [matches(query) for query in queries]
