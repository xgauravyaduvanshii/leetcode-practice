# LeetCode 830. Positions of Large Groups — Easy
# https://leetcode.com/problems/positions-of-large-groups/
# Submission 2197532308 — Accepted, Python3
#
# My thinking: I walk through the string keeping
# track of where the current run of the same letter
# started. When the letter changes (or I reach the
# end), I check how long that run was — if it is
# 3 or more, I record its start and end positions.

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        result = []
        n = len(s)
        start = 0
        for i in range(1, n + 1):
            if i == n or s[i] != s[start]:
                if i - start >= 3:
                    result.append([start, i - 1])
                start = i
        return result
