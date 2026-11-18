# LeetCode 2974. Minimum Number Game — Easy
# https://leetcode.com/problems/minimum-number-game/
# Submission 2198712992 — Accepted, Python3
#
# My thinking: Alice and Bob keep taking the two
# smallest numbers left, and Bob's number lands
# before Alice's in the answer. Sorting the array
# and swapping each neighbouring pair does exactly
# that.

from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []
        for i in range(0, len(nums), 2):
            answer.append(nums[i + 1])
            answer.append(nums[i])
        return answer
