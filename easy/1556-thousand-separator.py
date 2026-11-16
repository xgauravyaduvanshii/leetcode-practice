# LeetCode 1556. Thousand Separator — Easy
# https://leetcode.com/problems/thousand-separator/
# Submission 2197585711 — Accepted, Python3
#
# My thinking: Python's format spec already groups
# digits in threes with commas. I just format the
# number that way and swap the commas for dots.

class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:,}".replace(",", ".")
