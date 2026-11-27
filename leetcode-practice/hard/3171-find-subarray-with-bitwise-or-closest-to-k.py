# LeetCode 3171. Find Subarray With Bitwise OR Closest to K — Hard
# https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/
# Submission 2202057474 — Accepted, Python3
#
# My thinking: the ORs of subarrays
# ending at each position are few — OR
# only gains bits, so at most 32 distinct
# values survive. I keep that small set,
# extend it with each new element, and
# track the closest value to k as I go.

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = 10 ** 18
        cur = set()
        for x in nums:
            nxt = {x}
            for v in cur:
                nxt.add(v | x)
            cur = nxt
            for v in cur:
                d = k - v
                if d < 0:
                    d = -d
                if d < ans:
                    ans = d
                    if ans == 0:
                        return 0
        return ans
