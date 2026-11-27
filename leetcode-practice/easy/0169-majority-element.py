# LeetCode 169. Majority Element — Easy
# https://leetcode.com/problems/majority-element/
# Submission 2197448324 — Accepted, Python3
#
# My thinking: Boyer-Moore voting. I keep a candidate
# and a count. Every time I see the candidate I add
# one, otherwise I take one away. When the count hits
# zero I pick a new candidate. The majority element
# appears more than half the time, so it cannot be
# voted out completely — it is the one left at the end.

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
