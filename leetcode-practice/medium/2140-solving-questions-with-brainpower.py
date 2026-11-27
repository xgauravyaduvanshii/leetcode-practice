# LeetCode 2140. Solving Questions With Brainpower — Medium
# https://leetcode.com/problems/solving-questions-with-brainpower/
# Submission 2204473206 — Accepted, Python3
#
# My thinking: at each question I either solve it, gaining its points
# and skipping the next brainpower questions, or skip it and move to the
# next one. The best score from position i is the better of those two
# choices, so I fill a table backwards from the last question and the
# answer is the value at position 0.
class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            nxt = i + brainpower + 1
            take = points + (dp[nxt] if nxt <= n else 0)
            skip = dp[i + 1]
            dp[i] = take if take > skip else skip
        return dp[0]
