# LeetCode 873. Length of Longest Fibonacci Subsequence — Medium
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# Submission 2198960624 — Accepted, Python3
#
# My thinking: every pair of numbers starts a
# possible sequence, and the next number is
# forced — the sum of the last two. I follow each
# pair as far as it goes and keep the longest.

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        values = set(arr)
        best = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                first, second = arr[i], arr[j]
                length = 2
                while first + second in values:
                    first, second = second, first + second
                    length += 1
                best = max(best, length)
        return best if best > 2 else 0
