# LeetCode 224. Basic Calculator — Hard
# https://leetcode.com/problems/basic-calculator/
# Submission 2198396093 — Accepted, Python3
#
# My thinking: I read the expression left to right
# keeping a running total and the current sign. A
# number is added with that sign; an opening
# bracket saves the total and sign so far and
# starts a fresh sum inside; a closing bracket
# applies the saved sign to the bracket's sum and
# adds it back to the saved total.

class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        sign = 1
        stack = []
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                total += sign * num
                continue
            elif ch == "+":
                sign = 1
            elif ch == "-":
                sign = -1
            elif ch == "(":
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1
            elif ch == ")":
                total *= stack.pop()
                total += stack.pop()
            i += 1
        return total
