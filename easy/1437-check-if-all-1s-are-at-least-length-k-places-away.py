# LeetCode 1437. Check If All 1's Are at Least Length K Places Away — Easy
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# Submission 2197579041 — Accepted, Python3
#
# My thinking: I remember where the last 1 was. Each
# time I meet a new 1, I count the zeros between
# them — if there are fewer than k, the answer is
# false. If I get through the whole array, it is true.

class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last = -1
        for i, x in enumerate(nums):
            if x == 1:
                if last != -1 and i - last - 1 < k:
                    return False
                last = i
        return True
