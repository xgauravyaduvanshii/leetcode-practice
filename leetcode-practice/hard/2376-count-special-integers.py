# LeetCode 2376. Count Special Integers — Hard
# https://leetcode.com/problems/count-special-integers/
# Submission 2201702709 — Accepted, Python3
#
# My thinking: shorter numbers are counted
# by choosing distinct digits, and numbers
# as long as n are counted digit by digit
# — at each step I may pick any unused
# digit below n's, then fill the rest
# freely from what is left.

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digits = list(map(int, str(n)))
        L = len(digits)
        ans = 0
        for length in range(1, L):
            count = 9
            avail = 9
            for _ in range(1, length):
                count *= avail
                avail -= 1
            ans += count
        used = [False] * 10
        for i, d in enumerate(digits):
            remaining = L - i - 1
            start = 1 if i == 0 else 0
            for smaller in range(start, d):
                if used[smaller]:
                    continue
                count = 1
                avail = 10 - i - 1
                for _ in range(remaining):
                    count *= avail
                    avail -= 1
                ans += count
            if used[d]:
                return ans
            used[d] = True
        ans += 1
        return ans
