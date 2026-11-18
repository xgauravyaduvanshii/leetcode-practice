# LeetCode 1006. Clumsy Factorial — Medium
# https://leetcode.com/problems/clumsy-factorial/
# Submission 2198984091 — Accepted, Python3
#
# My thinking: the operations repeat in groups of
# four — multiply, divide, add, subtract. The
# first group is added, and every later group is
# subtracted as a whole, with a small tail left
# over at the end.

class Solution:
    def clumsy(self, n: int) -> int:
        if n <= 2:
            return n
        if n == 3:
            return 6
        total = n * (n - 1) // (n - 2) + (n - 3)
        n -= 4
        while n >= 4:
            total -= n * (n - 1) // (n - 2)
            total += n - 3
            n -= 4
        if n == 3:
            total -= 6
        elif n == 2:
            total -= 2
        elif n == 1:
            total -= 1
        return total
