# LeetCode 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers — Medium
# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# Submission 2199913213 — Accepted, Python3
#
# My thinking: each deci-binary number can
# give at most 1 to every digit. The biggest
# digit decides how many numbers I need, and
# that many always suffice.

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(ch) for ch in n)
