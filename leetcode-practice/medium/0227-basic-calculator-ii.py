# LeetCode 227. Basic Calculator II — Medium
# https://leetcode.com/problems/basic-calculator-ii/
# Submission 2198461290 — Accepted, Python3
#
# My thinking: I read the expression once, keeping
# the number I am building and the last operator I
# saw. When the next operator (or the end) arrives,
# I apply the last operator to the number: + and -
# push it onto a stack, * and / combine it with the
# stack's top straight away, which is what gives
# them priority. Adding up the stack at the end
# gives the answer, with division truncating toward
# zero.

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                sign = ch
                num = 0
        return sum(stack)
