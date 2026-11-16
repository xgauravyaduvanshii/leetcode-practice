# LeetCode 2231. Largest Number After Digit Swaps by Parity — Easy
# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
# Submission 2197618840 — Accepted, Python3
#
# My thinking: odd digits can only swap with odd
# digits and even with even, keeping their positions'
# parity. To make the number as large as possible, I
# sort the odd digits and the even digits each from
# biggest to smallest, then place them back into the
# positions of their own parity.

class Solution:
    def largestInteger(self, num: int) -> int:
        s = list(str(num))
        odds = sorted([c for c in s if int(c) % 2 == 1], reverse=True)
        evens = sorted([c for c in s if int(c) % 2 == 0], reverse=True)
        oi = ei = 0
        for i, c in enumerate(s):
            if int(c) % 2 == 1:
                s[i] = odds[oi]
                oi += 1
            else:
                s[i] = evens[ei]
                ei += 1
        return int(''.join(s))
