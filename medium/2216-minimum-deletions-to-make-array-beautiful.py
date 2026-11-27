# LeetCode 2216. Minimum Deletions to Make Array Beautiful — Medium
# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/
# Submission 2204505346 — Accepted, Python3
#
# My thinking: a beautiful array has even length and no equal neighbours
# at even-odd pairs. I rebuild the array greedily, keeping an element
# only when it does not repeat the previous kept element at an odd
# position; a repeated element is deleted. If the rebuilt array ends up
# odd, I drop its last element, and the deletions are the difference in
# length.
class Solution:
    def minDeletion(self, nums: list[int]) -> int:
        kept = []
        for x in nums:
            if len(kept) % 2 == 1 and kept[-1] == x:
                continue
            kept.append(x)
        if len(kept) % 2 == 1:
            kept.pop()
        return len(nums) - len(kept)
