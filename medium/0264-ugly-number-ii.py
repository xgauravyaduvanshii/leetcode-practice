# LeetCode 264. Ugly Number II — Medium
# https://leetcode.com/problems/ugly-number-ii/
# Submission 2198726722 — Accepted, Python3
#
# My thinking: every ugly number is an earlier ugly
# number times 2, 3 or 5. I keep three pointers, one
# per factor, and always take the smallest next
# candidate — moving every pointer that produced it
# so no number is ever repeated.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            ugly.append(next_ugly)
            if next_ugly == ugly[i2] * 2:
                i2 += 1
            if next_ugly == ugly[i3] * 3:
                i3 += 1
            if next_ugly == ugly[i5] * 5:
                i5 += 1
        return ugly[-1]
