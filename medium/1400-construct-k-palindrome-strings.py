# LeetCode 1400. Construct K Palindrome Strings — Medium
# https://leetcode.com/problems/construct-k-palindrome-strings/
# Submission 2199049288 — Accepted, Python3
#
# My thinking: each palindrome can hold at most
# one letter with an odd count. So the string
# works when its odd-count letters are no more
# than k — and k cannot exceed the string
# length.

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        odd = sum(count % 2 for count in Counter(s).values())
        return odd <= k
