# LeetCode 1545. Find Kth Bit in Nth Binary String — Medium
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
# Submission 2199872278 — Accepted, Python3
#
# My thinking: each string is the previous one,
# a "1", then the inverted reverse of the
# previous one. I zoom into the half holding
# position k, flipping my answer whenever I
# cross into the mirrored half.

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = (1 << n) - 1
        flip = False
        while length > 1:
            mid = (length + 1) // 2
            if k == mid:
                return "0" if flip else "1"
            if k > mid:
                k = length - k + 1
                flip = not flip
            length = mid - 1
        return "1" if flip else "0"
