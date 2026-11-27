# LeetCode 2389. Longest Subsequence With Limited Sum — Easy
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/
# Submission 2197776916 — Accepted, Python3
#
# My thinking: to fit the most numbers under a limit
# I should take the smallest ones first, so I sort
# the array and build prefix sums. For each query
# the answer is how many prefix sums fit under it,
# found with binary search.

import bisect


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        return [bisect.bisect_right(prefix, q) - 1 for q in queries]
