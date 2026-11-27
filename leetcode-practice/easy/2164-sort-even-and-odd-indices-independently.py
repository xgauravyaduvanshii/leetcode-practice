# 2164. Sort Even and Odd Indices Independently (Easy)
# https://leetcode.com/problems/sort-even-and-odd-indices-independently/
# Submission 2199968492 — Accepted, Python3
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # My thinking: split the numbers by their index
        # — even spots in one pile, odd spots in another.
        # Sort the even pile rising and the odd pile
        # falling, then weave them back together.
        evens = sorted(nums[0::2])
        odds = sorted(nums[1::2], reverse=True)
        answer = []
        for i in range(len(nums)):
            if i % 2 == 0:
                answer.append(evens[i // 2])
            else:
                answer.append(odds[i // 2])
        return answer
