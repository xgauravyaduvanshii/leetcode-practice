# LeetCode 2381. Shifting Letters II — Medium
# https://leetcode.com/problems/shifting-letters-ii/
# Submission 2204770286 — Accepted, Python3
#
# My thinking: range shifts are handled with a difference array — each
# shift adds +1 or -1 at its start and cancels it just past its end.
# One prefix-sum pass then gives the total shift per position, applied
# modulo 26 to each letter.
class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for start, end, direction in shifts:
            d = 1 if direction == 1 else -1
            diff[start] += d
            diff[end + 1] -= d
        res = []
        cur = 0
        for i, ch in enumerate(s):
            cur += diff[i]
            res.append(chr((ord(ch) - 97 + cur) % 26 + 97))
        return ''.join(res)
