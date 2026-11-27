# LeetCode 2160. Minimum Sum of Four Digit Number After Splitting Digits — Easy
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
# Submission 2197615952 — Accepted, Python3
#
# My thinking: I sort the four digits. The two
# smallest digits should be the tens digits of the
# two numbers I build, and the two largest digits
# their ones digits — that keeps the sum as small as
# possible.

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))
        return int(digits[0] + digits[2]) + int(digits[1] + digits[3])
