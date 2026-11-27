# LeetCode 1652. Defuse the Bomb — Easy
# https://leetcode.com/problems/defuse-the-bomb/
# Submission 2197591954 — Accepted, Python3
#
# My thinking: if k is 0, every answer is 0. If k
# is positive, each position sums the next k
# numbers (wrapping around the circle); if k is
# negative, it sums the previous |k| numbers. I
# just add them up directly.

class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        result = []
        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            else:
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]
            result.append(total)
        return result
