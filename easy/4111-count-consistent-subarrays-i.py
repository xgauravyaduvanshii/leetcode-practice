# 4111. Count Consistent Subarrays I (Easy)
# https://leetcode.com/problems/count-consistent-subarrays-i/
# Submission 2200105508 — Accepted, Python3
class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        # My thinking: I try every subarray, tracking
        # its bitwise AND and its minimum as I extend
        # it — the subarray counts when the two agree.
        ans = 0
        n = len(nums)
        for i in range(n):
            and_val = nums[i]
            min_val = nums[i]
            for j in range(i, n):
                and_val &= nums[j]
                min_val = min(min_val, nums[j])
                if and_val == min_val:
                    ans += 1
        return ans
