# LeetCode 1718. Construct the Lexicographically Largest Valid Sequence — Medium
# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/
# Submission 2199920297 — Accepted, Python3
#
# My thinking: I fill the sequence left to
# right, always trying the biggest unused
# number that fits — a number k needs its
# second copy exactly k spots later. Backtrack
# when a choice leaves no way forward.

from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        result = [0] * size
        used = [False] * (n + 1)

        def backtrack(pos):
            if pos == size:
                return True
            if result[pos] != 0:
                return backtrack(pos + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    result[pos] = 1
                    used[1] = True
                    if backtrack(pos + 1):
                        return True
                    result[pos] = 0
                    used[1] = False
                elif pos + num < size and result[pos + num] == 0:
                    result[pos] = num
                    result[pos + num] = num
                    used[num] = True
                    if backtrack(pos + 1):
                        return True
                    result[pos] = 0
                    result[pos + num] = 0
                    used[num] = False
            return False

        backtrack(0)
        return result
