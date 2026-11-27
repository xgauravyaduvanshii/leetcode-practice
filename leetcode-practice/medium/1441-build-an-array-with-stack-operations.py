# LeetCode 1441. Build an Array With Stack Operations — Medium
# https://leetcode.com/problems/build-an-array-with-stack-operations/
# Submission 2197579315 — Accepted, Python3
#
# My thinking: I walk the numbers 1, 2, 3... and for
# each target value I push and pop every number
# before it (they are not wanted), then push the
# target value itself and move on. That builds the
# target list with the fewest operations.

class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result = []
        current = 1
        for value in target:
            while current < value:
                result.append("Push")
                result.append("Pop")
                current += 1
            result.append("Push")
            current += 1
        return result
