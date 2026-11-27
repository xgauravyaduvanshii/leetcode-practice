# LeetCode 202. Happy Number — Easy
# https://leetcode.com/problems/happy-number/
# Submission 2197449902 — Accepted, Python3
#
# My thinking: I keep replacing the number with the
# sum of the squares of its digits. If I ever reach
# 1, it is happy. If I see a number I have already
# seen, I am going in a loop and it will never
# reach 1 — so I remember every number I visit.

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1
