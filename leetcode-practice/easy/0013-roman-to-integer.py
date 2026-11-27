# LeetCode 13. Roman to Integer — Easy
# https://leetcode.com/problems/roman-to-integer/
# Submission 2197268013 — Accepted, Python3
#
# My thinking: I go through the string from right to left.
# Normally I just add the value. But if a smaller symbol
# comes before a bigger one, like I before V, that means
# subtract — so I subtract it instead.

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
        }

        total = 0
        previous_value = 0

        for letter in reversed(s):
            current_value = values[letter]

            if current_value < previous_value:
                # like IV = 4, not 6
                total -= current_value
            else:
                total += current_value

            previous_value = current_value

        return total
