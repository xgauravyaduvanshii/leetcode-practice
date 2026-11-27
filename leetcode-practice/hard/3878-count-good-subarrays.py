# LeetCode 3878. Count Good Subarrays — Hard
# https://leetcode.com/problems/count-good-subarrays/
# Submission 2203337074 — Accepted, Python3
from typing import List


class Solution:
    def countGoodSubarrays(self, nums: List[int]) -> int:
        # My thinking: a subarray is good exactly when its
        # bitwise OR equals one of its elements. The OR is
        # numerically at least as large as every element in
        # the subarray, so it can only equal an element that
        # carries all of the OR's bits — that is, an element
        # equal to the OR itself. Fix the right end r: the
        # distinct ORs of subarrays ending at r are at most
        # 30, each covering a contiguous range of left ends.
        # For a group with OR v, the subarrays in it are
        # good exactly for the left ends at or before the
        # latest occurrence of v, which a hash map tracks as
        # r moves. The answer can reach about n^2 / 2, so it
        # is a plain Python int.
        ans = 0
        ors = []
        last = {}
        for r, x in enumerate(nums):
            last[x] = r
            new_ors = [[x, 1]]
            for v, c in ors:
                nv = v | x
                if nv == new_ors[-1][0]:
                    new_ors[-1][1] += c
                else:
                    new_ors.append([nv, c])
            ors = new_ors
            end = r
            for v, c in ors:
                start = end - c + 1
                p = last.get(v, -1)
                if p >= start:
                    ans += min(end, p) - start + 1
                end = start - 1
        return ans
