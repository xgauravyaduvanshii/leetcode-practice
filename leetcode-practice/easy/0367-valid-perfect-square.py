# LeetCode 367. Valid Perfect Square — Easy
# https://leetcode.com/problems/valid-perfect-square/
# Submission 2197468724 — Accepted, Python3
#
# My thinking: binary search for the square root. I
# try the middle number — if its square is the
# target, I found it; if it is too small, I search
# the upper half; if too big, the lower half. If the
# search runs out, it is not a perfect square.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            if square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
