# LeetCode 2455. Average Value of Even Numbers That Are Divisible by Three — Easy
# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
# Submission 2197788290 — Accepted, Python3
#
# My thinking: even and divisible by three means
# divisible by six. I average those numbers, and if
# there are none the answer is 0.

class Solution:
    def averageValue(self, nums: list[int]) -> int:
        vals = [x for x in nums if x % 6 == 0]
        return sum(vals) // len(vals) if vals else 0
