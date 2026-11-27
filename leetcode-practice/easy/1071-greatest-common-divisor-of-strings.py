# LeetCode 1071. Greatest Common Divisor of Strings — Easy
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Submission 2197555255 — Accepted, Python3
#
# My thinking: for one string to divide both, the
# two strings have to be built from the same
# repeating piece — so str1 + str2 must equal
# str2 + str1. If that holds, the biggest such
# piece has the length of the GCD of the two
# lengths.

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]
