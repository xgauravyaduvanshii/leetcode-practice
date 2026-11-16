# LeetCode 1207. Unique Number of Occurrences — Easy
# https://leetcode.com/problems/unique-number-of-occurrences/
# Submission 2197563150 — Accepted, Python3
#
# My thinking: I count how many times each number
# appears. If any two numbers appear the same
# number of times, the answer is false — so the
# counts themselves must all be different, which I
# check by comparing the list of counts with the
# set of counts.

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = list(Counter(arr).values())
        return len(set(counts)) == len(counts)
