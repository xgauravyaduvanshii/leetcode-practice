# LeetCode 1313. Decompress Run-Length Encoded List — Easy
# https://leetcode.com/problems/decompress-run-length-encoded-list/
# Submission 2197569540 — Accepted, Python3
#
# My thinking: the list comes in pairs — a count
# followed by a value. For each pair I just repeat
# the value that many times and add it to the answer.

class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(0, len(nums), 2):
            result.extend([nums[i + 1]] * nums[i])
        return result
