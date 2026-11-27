# LeetCode 319. Bulb Switcher — Medium
# https://leetcode.com/problems/bulb-switcher/
# Submission 2198745161 — Accepted, Python3
#
# My thinking: a bulb is toggled once per divisor
# of its number, and divisors come in pairs — except
# for perfect squares, which have one unpaired
# divisor. So exactly the square-numbered bulbs stay
# on, and the answer is how many squares fit in n.

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)
