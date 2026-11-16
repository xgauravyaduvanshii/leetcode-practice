# LeetCode 374. Guess Number Higher or Lower — Easy
# https://leetcode.com/problems/guess-number-higher-or-lower/
# Submission 2197469405 — Accepted, Python3
#
# My thinking: plain binary search, using the guess
# API as my guide. I try the middle number — 0 means
# I found it, -1 means my guess was too high so I
# go lower, 1 means too low so I go higher.

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res < 0:
                right = mid - 1
            else:
                left = mid + 1
