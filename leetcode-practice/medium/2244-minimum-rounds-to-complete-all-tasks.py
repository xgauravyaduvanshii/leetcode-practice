# LeetCode 2244. Minimum Rounds to Complete All Tasks — Medium
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
# Submission 2204515236 — Accepted, Python3
#
# My thinking: tasks of the same difficulty are finished in rounds of 2
# or 3, so I count how many of each difficulty there are. A lone task
# can never be finished, so that means -1. Otherwise a count of c needs
# c // 3 rounds, plus one more round when c leaves a remainder of 1 or
# 2 — three 3s and a 2, or two 2s, cover the remainder.
class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        from collections import Counter
        ans = 0
        for c in Counter(tasks).values():
            if c == 1:
                return -1
            ans += c // 3 + (1 if c % 3 else 0)
        return ans
