# LeetCode 640. Solve the Equation — Medium
# https://leetcode.com/problems/solve-the-equation/
# Submission 2198890237 — Accepted, Python3
#
# My thinking: I read each side into how many x's
# it has and what plain number is left, then move
# everything to one side. Equal sides with no x
# means every x works, or none does.

class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(side):
            x_coeff = 0
            constant = 0
            number = ""
            sign = 1
            for char in side + "+":
                if char.isdigit():
                    number += char
                elif char == "x":
                    x_coeff += sign * (int(number) if number else 1)
                    number = ""
                elif char in "+-":
                    if number:
                        constant += sign * int(number)
                        number = ""
                    sign = 1 if char == "+" else -1
            return x_coeff, constant

        left, right = equation.split("=")
        lx, lc = parse(left)
        rx, rc = parse(right)
        coeff = lx - rx
        const = rc - lc
        if coeff == 0:
            return "Infinite solutions" if const == 0 else "No solution"
        return f"x={const // coeff}"
