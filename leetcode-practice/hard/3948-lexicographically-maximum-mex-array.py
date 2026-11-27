# LeetCode 3948. Lexicographically Maximum MEX Array — Hard
# https://leetcode.com/problems/lexicographically-maximum-mex-array/
# Submission 2203444608 — Accepted, Python3
from typing import List


class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        # My thinking: the MEX of a growing prefix never drops,
        # so the biggest first element we can ever produce is
        # the MEX of the whole remaining suffix — and the
        # shortest cut achieving it ends just after the last
        # of 0..MEX-1 first shows up. Taking that shortest cut
        # is also best for the rest: any longer first cut leaves
        # a suffix of the same tail, and the extra elements it
        # swallows can only raise the next MEX, never lower it.
        # So repeat: append the suffix MEX, cut right after its
        # last missing value appears (or after one element when
        # the MEX is 0). A frequency table of the suffix keeps
        # the MEX current as the start moves forward — removing
        # elements can only lower it — and each scan for the cut
        # advances the start, so the whole run is linear.
        n = len(nums)
        freq = [0] * (n + 2)
        for v in nums:
            if v <= n:
                freq[v] += 1
        mex = 0
        while mex <= n and freq[mex] > 0:
            mex += 1
        res = []
        s = 0
        while s < n:
            m = mex
            if m == 0:
                res.append(0)
                v = nums[s]
                if v <= n:
                    freq[v] -= 1
                    if freq[v] == 0 and v < mex:
                        mex = v
                s += 1
                continue
            seen = [False] * m
            got = 0
            i = s
            while got < m:
                v = nums[i]
                if v < m and not seen[v]:
                    seen[v] = True
                    got += 1
                i += 1
            k = i
            res.append(m)
            for j in range(s, k):
                v = nums[j]
                if v <= n:
                    freq[v] -= 1
                    if freq[v] == 0 and v < mex:
                        mex = v
            s = k
        return res
