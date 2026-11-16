# LeetCode 350. Intersection of Two Arrays II — Easy
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Submission 2197468205 — Accepted, Python3
#
# My thinking: unlike problem 349, duplicates count
# here. So I count how many times each number appears
# in the first list, then go through the second list
# and take a number only while I still have some of
# it left — using one up each time.

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = {}
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
        result = []
        for num in nums2:
            if counts.get(num, 0) > 0:
                result.append(num)
                counts[num] -= 1
        return result
