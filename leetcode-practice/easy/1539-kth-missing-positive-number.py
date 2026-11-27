# LeetCode 1539. Kth Missing Positive Number — Easy
# https://leetcode.com/problems/kth-missing-positive-number/
# Submission 2197585003 — Accepted, Python3
#
# My thinking: I walk through the sorted array with
# my target k in hand. Every array number that is
# at most k takes one of the missing slots, so k
# shifts up by one. When I meet a number bigger
# than k, nothing after it can matter — k is the
# answer.

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        for x in arr:
            if x <= k:
                k += 1
            else:
                break
        return k
