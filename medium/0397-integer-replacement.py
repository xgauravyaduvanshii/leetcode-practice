# LeetCode 397. Integer Replacement — Medium
# https://leetcode.com/problems/integer-replacement/
# Submission 2198775580 — Accepted, Python3
#
# My thinking: even numbers just halve. For an odd
# number I look at the last two bits — going down is
# better when the number is 3 or ends in 01, going up
# when it ends in 11, because that clears more ones
# at once.

class Solution:
    def integerReplacement(self, n: int) -> int:
        steps = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
            steps += 1
        return steps
