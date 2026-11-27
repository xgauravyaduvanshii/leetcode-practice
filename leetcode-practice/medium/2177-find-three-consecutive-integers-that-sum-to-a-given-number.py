# LeetCode 2177. Find Three Consecutive Integers That Sum to a Given Number — Medium
# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
# Submission 2204487192 — Accepted, Python3
#
# My thinking: three consecutive integers x, x+1, x+2 sum to 3x + 3, so
# the middle one must be num / 3. That only works when num is divisible
# by 3; otherwise no such triple exists and I return an empty list.
class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3 != 0:
            return []
        x = num // 3 - 1
        return [x, x + 1, x + 2]
