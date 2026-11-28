# LeetCode 2429. Minimize XOR — Medium
# https://leetcode.com/problems/minimize-xor/
# Submission 2204863398 — Accepted, Python3
#
# My thinking: x needs exactly as many set bits as num2 has. To make
# x XOR num1 as small as possible, take num1's set bits first, from
# the highest bit down — matching num1 where it matters most. Any
# bits still needed go on the lowest unset positions, where they add
# the least.
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        need = bin(num2).count("1")
        x = 0
        for b in range(30, -1, -1):
            if need and (num1 >> b) & 1:
                x |= 1 << b
                need -= 1
        for b in range(31):
            if need and not (x >> b) & 1:
                x |= 1 << b
                need -= 1
        return x
