# LeetCode 1898. Maximum Number of Removable Characters — Medium
# https://leetcode.com/problems/maximum-number-of-removable-characters/
# Submission 2201090940 — Accepted, Python3
#
# My thinking: p is a subsequence of s, and removing
# more characters can only break that, so I binary-search
# the largest prefix of removable I can delete while p
# still shows up in what is left.

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def is_subsequence(k):
            removed = set(removable[:k])
            j = 0
            for i, ch in enumerate(s):
                if i in removed:
                    continue
                if j < len(p) and ch == p[j]:
                    j += 1
            return j == len(p)
        left, right = 0, len(removable)
        while left < right:
            mid = (left + right + 1) // 2
            if is_subsequence(mid):
                left = mid
            else:
                right = mid - 1
        return left
