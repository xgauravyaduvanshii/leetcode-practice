# LeetCode 1287. Element Appearing More Than 25% In Sorted Array — Easy
# https://leetcode.com/problems/element-appearing-more-than-25-percent-in-sorted-array/
# Submission 2197567317 — Accepted, Python3
#
# My thinking: the special element appears in more
# than a quarter of the array. I count each value
# and return the first one whose count beats a
# quarter of the length — exactly one element can
# do that.

from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        counts = Counter(arr)
        threshold = len(arr) // 4
        for num, count in counts.items():
            if count > threshold:
                return num
        return arr[0]
