# LeetCode 2147. Number of Ways to Divide a Long Corridor — Hard
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
# Submission 2201588296 — Accepted, Python3
#
# My thinking: every section needs exactly two
# seats, so the dividers are forced to fall
# between the pairs — and between one pair and
# the next, any of the empty gaps will do, so
# the choices multiply.

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        if len(seats) == 0 or len(seats) % 2 == 1:
            return 0
        ans = 1
        for i in range(1, len(seats) - 1, 2):
            ans = ans * (seats[i + 1] - seats[i]) % MOD
        return ans
