# LeetCode 2917. Find the K-or of an Array — Easy
# https://leetcode.com/problems/find-the-k-or-of-an-array/
# Submission 2198696002 — Accepted, Python3
#
# My thinking: each bit of the answer is decided on
# its own — a bit is set exactly when at least k
# numbers have that bit set. I check all 31 bits and
# build the answer from the ones that qualify.

from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        answer = 0
        for bit in range(31):
            count = sum(1 for num in nums if num >> bit & 1)
            if count >= k:
                answer |= 1 << bit
        return answer
