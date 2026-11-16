# LeetCode 852. Peak Index in a Mountain Array — Medium
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Submission 2197535057 — Accepted, Python3
#
# My thinking: the array climbs up to the peak and
# then goes down. Binary search works here: if the
# middle is smaller than the next one, the peak is
# to the right; otherwise it is at the middle or to
# the left. I keep shrinking the range until it
# lands on the peak.

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
