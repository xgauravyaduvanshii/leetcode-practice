# 3875. Construct Uniform Parity Array I (Easy)
# https://leetcode.com/problems/construct-uniform-parity-array-i/
# Submission 2200083546 — Accepted, Python3
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # My thinking: the answer is always yes. If
        # there is any odd number, make everything odd
        # — odd numbers stay as they are, and each even
        # number minus that odd number turns odd. If
        # there is no odd number at all, everything is
        # already even.
        return True
