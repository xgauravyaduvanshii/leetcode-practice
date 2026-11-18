# LeetCode 2928. Distribute Candies Among Children I — Easy
# https://leetcode.com/problems/distribute-candies-among-children-i/
# Submission 2198701482 — Accepted, Python3
#
# My thinking: with only n up to 50 I can just try
# every split — how many the first child gets, how
# many the second gets — and count the ones where
# the third child's share stays within the limit.

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for first in range(min(n, limit) + 1):
            for second in range(min(n - first, limit) + 1):
                if n - first - second <= limit:
                    count += 1
        return count
