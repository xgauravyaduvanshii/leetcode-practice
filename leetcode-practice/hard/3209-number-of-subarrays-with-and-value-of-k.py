# LeetCode 3209. Number of Subarrays With AND Value of K — Hard
# https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/
# Submission 2202080976 — Accepted, Python3
#
# My thinking: the ANDs of subarrays
# ending at each position are few — AND
# only clears bits, so at most 32
# distinct values survive. I keep that
# small map of value to count, extend it
# with each new element, and add the
# count of subarrays whose AND equals k.

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        prev = {}
        for x in nums:
            cur = {x: 1}
            for val, cnt in prev.items():
                nv = val & x
                cur[nv] = cur.get(nv, 0) + cnt
            ans += cur.get(k, 0)
            prev = cur
        return ans
