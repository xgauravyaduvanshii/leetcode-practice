# LeetCode 1963. Minimum Number of Swaps to Make the String Balanced — Medium
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
# Submission 2204261560 — Accepted, Python3
#
# My thinking: I scan the string keeping a balance of open brackets
# seen so far. A closing bracket when the balance is zero means an
# unmatched ']' — one swap with a later '[' fixes it, so I count a
# swap and treat the balance as if that '[' had been there instead.
# Every such unmatched closer needs its own swap, and the swaps I
# count are exactly the minimum, because each swap can fix at most
# one unmatched closer.
class Solution:
    def minSwaps(self, s):
        balance = 0
        swaps = 0
        for ch in s:
            if ch == "[":
                balance += 1
            elif balance == 0:
                swaps += 1
                balance += 1
            else:
                balance -= 1
        return swaps
