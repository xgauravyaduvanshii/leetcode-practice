# LeetCode 682. Baseball Game — Easy
# https://leetcode.com/problems/baseball-game/
# Submission 2197514276 — Accepted, Python3
#
# My thinking: I keep a running list of the scores.
# A number just gets added. "D" doubles the last
# score, "C" removes the last score, and "+" adds
# the last two scores together. At the end I add
# up whatever is left in the list.

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                record.append(record[-1] + record[-2])
            elif op == "D":
                record.append(2 * record[-1])
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        return sum(record)
