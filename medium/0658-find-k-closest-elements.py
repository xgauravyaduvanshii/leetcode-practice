# LeetCode 658. Find K Closest Elements — Medium
# https://leetcode.com/problems/find-k-closest-elements/
# Submission 2198900932 — Accepted, Python3
#
# My thinking: the answer is one window of k
# consecutive numbers. I binary search for where
# that window starts — if the element just past
# the window is closer than the first one inside
# it, the window slides right.

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
