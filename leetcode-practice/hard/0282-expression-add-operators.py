# LeetCode 282. Expression Add Operators — Hard
# https://leetcode.com/problems/expression-add-operators/
# Submission 2198399060 — Accepted, Python3
#
# My thinking: I try every split of the digits into
# numbers, joining them with +, - or *. To get
# multiplication right I remember the last operand
# I added, so a * can undo it and multiply it
# instead. A number with a leading zero is only
# allowed as a single zero, and a full expression
# counts only when it reaches the target.

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        answer = []

        def dfs(index: int, expr: str, value: int, prev: int) -> None:
            if index == len(num):
                if value == target:
                    answer.append(expr)
                return
            for end in range(index + 1, len(num) + 1):
                part = num[index:end]
                if len(part) > 1 and part[0] == "0":
                    break
                current = int(part)
                if index == 0:
                    dfs(end, part, current, current)
                else:
                    dfs(end, expr + "+" + part, value + current, current)
                    dfs(end, expr + "-" + part, value - current, -current)
                    dfs(end, expr + "*" + part, value - prev + prev * current, prev * current)

        dfs(0, "", 0, 0)
        return answer
