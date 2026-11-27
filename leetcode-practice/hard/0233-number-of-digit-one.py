# LeetCode 233. Number of Digit One — Hard
# https://leetcode.com/problems/number-of-digit-one/
# Submission 2198396816 — Accepted, Python3
#
# My thinking: I count the ones one place at a time
# — units, tens, hundreds, and so on. For each
# place I split the number into the part above it,
# the digit at it, and the part below it. If the
# digit is 0, that place contributes one per full
# cycle above it; if it is 1, it adds the lower part
# plus one more; if it is bigger, it adds one more
# full cycle.

class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        place = 1
        while place <= n:
            high = n // (place * 10)
            digit = (n // place) % 10
            low = n % place
            if digit == 0:
                count += high * place
            elif digit == 1:
                count += high * place + low + 1
            else:
                count += (high + 1) * place
            place *= 10
        return count
