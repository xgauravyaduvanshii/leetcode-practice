# LeetCode 838. Push Dominoes — Medium
# https://leetcode.com/problems/push-dominoes/
# Submission 2198951988 — Accepted, Python3
#
# My thinking: I measure the push from the right
# and from the left separately. A push fades by
# one each step, and where the two pushes are
# equal the domino stays standing.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        force = 0
        for i, ch in enumerate(dominoes):
            if ch == "R":
                force = n
            elif ch == "L":
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] += force
        force = 0
        for i in range(n - 1, -1, -1):
            ch = dominoes[i]
            if ch == "L":
                force = n
            elif ch == "R":
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] -= force
        result = []
        for i, ch in enumerate(dominoes):
            if forces[i] > 0:
                result.append("R")
            elif forces[i] < 0:
                result.append("L")
            else:
                result.append(".")
        return "".join(result)
