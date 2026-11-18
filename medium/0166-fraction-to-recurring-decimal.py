# LeetCode 166. Fraction to Recurring Decimal — Medium
# https://leetcode.com/problems/fraction-to-recurring-decimal/
# Submission 2198434713 — Accepted, Python3
#
# My thinking: I do long division one digit at a
# time. The sign comes from whether exactly one of
# the numbers is negative. If a remainder repeats,
# everything from its first appearance repeats, so
# I remember where each remainder first showed up
# and wrap that stretch in brackets when it does.

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        whole, remainder = divmod(numerator, denominator)
        result = sign + str(whole)
        if remainder == 0:
            return result
        result += "."
        seen = {}
        decimals = []
        while remainder:
            if remainder in seen:
                decimals.insert(seen[remainder], "(")
                decimals.append(")")
                break
            seen[remainder] = len(decimals)
            remainder *= 10
            digit, remainder = divmod(remainder, denominator)
            decimals.append(str(digit))
        return result + "".join(decimals)
