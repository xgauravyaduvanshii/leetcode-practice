# LeetCode 3347. Maximum Frequency of an Element After Performing Operations II — Hard
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/
# Submission 2202397836 — Accepted, Python3
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # My thinking: sort nums. For a target value v, every element in
        # [v-k, v+k] can be turned into v, and elements already equal to v
        # cost no operation, so the frequency is eq(v) + min(numOperations,
        # inrange(v) - eq(v)). The in-range count only changes when v passes
        # nums[i]-k or nums[i]+k, so it is enough to try v = nums[i]-k,
        # nums[i]+k and nums[i] itself; each query is a binary search.
        nums.sort()
        cands = set()
        for v in nums:
            cands.add(v - k)
            cands.add(v + k)
            cands.add(v)
        ans = 0
        for v in cands:
            lo = bisect_left(nums, v - k)
            hi = bisect_right(nums, v + k)
            eq = bisect_right(nums, v) - bisect_left(nums, v)
            inrange = hi - lo
            ans = max(ans, eq + min(numOperations, inrange - eq))
        return ans
