# LeetCode 2525. Categorize Box According to Criteria — Easy
# https://leetcode.com/problems/categorize-box-according-to-criteria/
# Submission 2197798833 — Accepted, Python3
#
# My thinking: a box is bulky when any side is at
# least 10,000 or its volume is at least a billion;
# it is heavy when its mass is at least 100. The
# category follows from which of those two apply.

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 10 ** 9
        heavy = mass >= 100
        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"
