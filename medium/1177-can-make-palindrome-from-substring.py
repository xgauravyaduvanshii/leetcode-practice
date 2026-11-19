# LeetCode 1177. Can Make Palindrome from Substring — Medium
# https://leetcode.com/problems/can-make-palindrome-from-substring/
# Submission 2199009325 — Accepted, Python3
#
# My thinking: a substring can become a
# palindrome when at most one letter appears an
# odd number of times — or two, if I have a
# replacement to spare. I track odd counts with
# a bit mask prefix.

from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        masks = [0]
        for ch in s:
            masks.append(masks[-1] ^ (1 << (ord(ch) - 97)))
        result = []
        for left, right, k in queries:
            odd = bin(masks[right + 1] ^ masks[left]).count("1")
            result.append(odd // 2 <= k)
        return result
