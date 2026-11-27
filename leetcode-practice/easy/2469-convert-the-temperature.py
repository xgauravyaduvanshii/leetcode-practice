# LeetCode 2469. Convert the Temperature — Easy
# https://leetcode.com/problems/convert-the-temperature/
# Submission 2197789843 — Accepted, Python3
#
# My thinking: Kelvin is Celsius plus 273.15, and
# Fahrenheit is Celsius times 1.8 plus 32.

class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]
