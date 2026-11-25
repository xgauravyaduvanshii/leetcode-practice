# LeetCode 3739. Count Subarrays With Majority Element II — Hard
# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/
# Submission 2203140678 — Accepted, Python3
from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # My thinking: write target as +1 and every other value
        # as -1, so target is the majority of a subarray exactly
        # when that subarray sums to more than 0. With prefix
        # sums, a subarray ending here is good exactly when an
        # earlier prefix sum is smaller than the current one, so
        # I keep the earlier prefix sums in a Fenwick tree over
        # the shifted range [-n, n] and count how many of them
        # sit below the current sum as I sweep the array once.
        n = len(nums)
        size = 2 * n + 1
        bit = [0] * (size + 2)

        def add(i: int, delta: int) -> None:
            while i <= size:
                bit[i] += delta
                i += i & -i

        def prefix(i: int) -> int:
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        add(n + 1, 1)
        s = 0
        ans = 0
        for x in nums:
            s += 1 if x == target else -1
            ans += prefix(s + n)
            add(s + n + 1, 1)
        return ans
