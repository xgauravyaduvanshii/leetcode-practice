# LeetCode 219. Contains Duplicate II — Easy
# https://leetcode.com/problems/contains-duplicate-ii/
# Submission 2197453740 — Accepted, Python3
#
# My thinking: I remember the last index where I saw
# each number. When I see a number again, I check
# how far apart the two positions are — if it is k
# or less, I have found it.

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_seen = {}
        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i
        return False
