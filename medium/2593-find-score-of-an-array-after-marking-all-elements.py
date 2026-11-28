# LeetCode 2593. Find Score of an Array After Marking All Elements — Medium
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/
# Submission 2205091499 — Accepted, Python3
#
# My thinking: always take the smallest unmarked element next
# — sorting the indices by value (ties by index) gives that
# order. Taking an element marks it and its neighbours, so
# skip anything already marked.
class Solution:
    def findScore(self, nums: list[int]) -> int:
        n = len(nums)
        order = sorted(range(n), key=lambda i: (nums[i], i))
        marked = [False] * n
        score = 0
        for i in order:
            if marked[i]:
                continue
            score += nums[i]
            marked[i] = True
            if i > 0:
                marked[i - 1] = True
            if i < n - 1:
                marked[i + 1] = True
        return score
