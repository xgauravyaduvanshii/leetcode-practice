# LeetCode 60. Permutation Sequence — Hard
# https://leetcode.com/problems/permutation-sequence/
# Submission 2198380076 — Accepted, Python3
#
# My thinking: the permutations come in blocks of
# (n-1)! that all start with the same first digit,
# then blocks of (n-2)! for the second digit, and
# so on. So I count in factorials: at each step I
# divide what is left of k by the block size to
# pick the next digit, and keep the remainder for
# the digits after it.

from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        k -= 1
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        answer = []
        for i in range(n - 1, -1, -1):
            index = k // fact[i]
            k %= fact[i]
            answer.append(str(numbers.pop(index)))
        return "".join(answer)
