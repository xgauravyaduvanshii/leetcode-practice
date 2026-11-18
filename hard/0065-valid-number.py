# LeetCode 65. Valid Number — Hard
# https://leetcode.com/problems/valid-number/
# Submission 2198380750 — Accepted, Python3
#
# My thinking: I read the string once and keep
# track of what I have seen — a digit, a dot, an
# exponent. A sign is only allowed at the very
# start or right after the exponent, a dot only
# once and never after the exponent, and an
# exponent needs a digit before it and resets the
# digit check for what follows. At the end there
# must be at least one digit after the last
# exponent.

class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_e = False
        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch in "+-":
                if i != 0 and s[i - 1] not in "eE":
                    return False
            elif ch == ".":
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif ch in "eE":
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False
            else:
                return False
        return seen_digit
