# LeetCode 3748. Count Stable Subarrays — Hard
# https://leetcode.com/problems/count-stable-subarrays/
# Submission 2203151730 — Accepted, Python3
from typing import List


class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # My thinking: a subarray is stable exactly when it is
        # non-decreasing, so every position i belongs to one
        # maximal non-decreasing run. Let L[i] be the start of
        # the run ending at i and f(i) = i - L[i] + 1 the number
        # of stable subarrays ending at i. For a query [l, r]
        # the runs are the key: inside the run that contains l,
        # a stable subarray ending at i can only start at or
        # after l, contributing i - l + 1; past that run every
        # run starts at or after l, so each i contributes the
        # full f(i). A prefix sum of f answers the second part
        # in O(1), and the first part is a triangular number,
        # so each query is O(1) after one linear pass.
        n = len(nums)
        start = [0] * n
        for i in range(1, n):
            start[i] = start[i - 1] if nums[i] >= nums[i - 1] else i
        run_end = [0] * n
        j = 0
        while j < n:
            k = j
            while k + 1 < n and nums[k + 1] >= nums[k]:
                k += 1
            for t in range(j, k + 1):
                run_end[t] = k
            j = k + 1
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (i - start[i] + 1)
        ans = []
        for l, r in queries:
            e = min(r, run_end[l])
            cnt = e - l + 1
            first = cnt * (cnt + 1) // 2
            second = pref[r + 1] - pref[e + 1]
            ans.append(first + second)
        return ans
