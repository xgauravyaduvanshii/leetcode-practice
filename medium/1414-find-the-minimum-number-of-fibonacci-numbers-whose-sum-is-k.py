# LeetCode 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K — Medium
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
# Submission 2199054766 — Accepted, Python3
#
# My thinking: the greedy choice is always
# right here — take the biggest Fibonacci
# number that fits, then repeat on what is
# left. Zeckendorf's rule makes it optimal.

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = [1, 2]
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])
        count = 0
        for value in reversed(fibs):
            if value <= k:
                k -= value
                count += 1
        return count
