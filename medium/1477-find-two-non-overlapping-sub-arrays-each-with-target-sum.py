# LeetCode 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum — Medium
# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
# Submission 2199858166 — Accepted, Python3
#
# My thinking: I sweep once, remembering the
# shortest good subarray seen so far. When a
# subarray ending here hits the target, I pair
# it with the best one that ended before it
# started.

from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        running = 0
        best_ending = []
        best_so_far = float("inf")
        answer = float("inf")
        for i, value in enumerate(arr):
            running += value
            if running - target in prefix:
                start = prefix[running - target] + 1
                length = i - start + 1
                if start > 0 and best_ending[start - 1] != float("inf"):
                    answer = min(answer, best_ending[start - 1] + length)
                best_so_far = min(best_so_far, length)
            best_ending.append(best_so_far)
            prefix[running] = i
        return -1 if answer == float("inf") else answer
