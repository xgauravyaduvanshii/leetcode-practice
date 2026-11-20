# 3069. Distribute Elements Into Two Arrays I (Easy)
# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/
# Submission 2199973412 — Accepted, Python3
from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # My thinking: the first two numbers seed the two
        # arrays. Each next number joins the array whose
        # last number is bigger — and on a tie it joins
        # the first array. At the end I glue the second
        # array after the first.
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for num in nums[2:]:
            if arr1[-1] >= arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
        return arr1 + arr2
