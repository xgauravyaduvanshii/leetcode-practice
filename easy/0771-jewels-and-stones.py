# LeetCode 771. Jewels and Stones — Easy
# https://leetcode.com/problems/jewels-and-stones/
# Submission 2197526710 — Accepted, Python3
#
# My thinking: I put the jewel types in a set, then
# count how many of the stones are in that set —
# each stone that matches a jewel type counts once.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)
