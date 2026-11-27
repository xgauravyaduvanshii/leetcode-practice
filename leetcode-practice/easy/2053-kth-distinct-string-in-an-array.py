# LeetCode 2053. Kth Distinct String in an Array — Easy
# https://leetcode.com/problems/kth-distinct-string-in-an-array/
# Submission 2197611034 — Accepted, Python3
#
# My thinking: a string is distinct when it appears
# exactly once. I count every string, keep the ones
# with count 1 in their original order, and return
# the k-th of those — or an empty string if there
# are fewer than k.

from collections import Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counts = Counter(arr)
        distinct = [s for s in arr if counts[s] == 1]
        return distinct[k - 1] if k <= len(distinct) else ""
