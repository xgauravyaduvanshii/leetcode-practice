# LeetCode 537. Complex Number Multiplication — Medium
# https://leetcode.com/problems/complex-number-multiplication/
# Submission 2198853260 — Accepted, Python3
#
# My thinking: I split each number at the plus sign
# into its real and imaginary parts, multiply them
# out the way complex numbers multiply, and join
# the result back together.

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(num):
            real, imag = num.split("+")
            return int(real), int(imag[:-1])

        a, b = parse(num1)
        c, d = parse(num2)
        return f"{a * c - b * d}+{a * d + b * c}i"
