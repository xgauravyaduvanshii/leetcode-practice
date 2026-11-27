# 4078. Three Fibonacci Sum (Easy)
# https://leetcode.com/problems/three-fibonacci-sum/
# Submission 2200103367 — Accepted, Python3
class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        # My thinking: I build the Fibonacci numbers
        # up past n, then check whether any three
        # neighbours add up to exactly n.
        fibs = [0, 1]
        while fibs[-1] <= n:
            fibs.append(fibs[-1] + fibs[-2])
        return any(
            fibs[i] + fibs[i + 1] + fibs[i + 2] == n for i in range(len(fibs) - 2)
        )
