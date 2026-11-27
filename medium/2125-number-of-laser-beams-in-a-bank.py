# LeetCode 2125. Number of Laser Beams in a Bank — Medium
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
# Submission 2204408716 — Accepted, Python3
#
# My thinking: beams only connect devices in two consecutive rows
# that both have devices, and every pair across such rows forms a
# beam. So I remember the device count of the last non-empty row and
# add prev * current for each new non-empty row, skipping empty rows
# entirely.
class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        total = 0
        prev = 0
        for row in bank:
            cnt = row.count('1')
            if cnt:
                total += prev * cnt
                prev = cnt
        return total
