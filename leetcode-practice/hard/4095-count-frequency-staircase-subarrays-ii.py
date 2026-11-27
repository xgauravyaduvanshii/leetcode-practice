# LeetCode 4095. Count Frequency Staircase Subarrays II — Hard
# https://leetcode.com/problems/count-frequency-staircase-subarrays-ii/
# Submission 2203725499 — Accepted, Python3


class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        # My thinking: a subarray is a frequency staircase
        # when the distinct values, in the order they first
        # appear, have frequencies exactly 1, 2, 3, ..., k.
        # A staircase with k distinct values is at least
        # 1 + 2 + ... + k = k(k+1)/2 long, so k never exceeds
        # the largest K with K(K+1)/2 <= n. First, a sliding
        # window over distinct values gives limit[l], the
        # last index of the all-distinct stretch starting at
        # l. If that stretch is longer than K, then every
        # subarray starting at l already needs more than K
        # distinct values before it can close, so only the
        # singleton [l, l] can be a staircase — count it and
        # move on (this is the fast path that keeps the
        # whole scan fast). Otherwise extend r from l,
        # tracking for each distinct value how many times it
        # has appeared (freq) and how many it must reach
        # (req = its order of first appearance), plus a bad
        # counter of values that have not yet reached their
        # required count. A new value is fine only while the
        # distinct count stays <= K and the minimal staircase
        # length still fits in the array; a repeat that
        # overshoots its required count ends the scan, since
        # adding more of it can never fix the excess. Each
        # time bad hits 0 the frequencies are exactly
        # 1, 2, ..., distinct, so the subarray nums[l..r]
        # is a staircase and we count it.
        n = len(nums)
        K = 1
        while (K + 1) * (K + 2) // 2 <= n:
            K += 1
        size = max(nums) + 1
        limit = [0] * n
        in_window = [0] * size
        r = 0
        for l in range(n):
            if r < l:
                r = l
            while r < n and in_window[nums[r]] == 0:
                in_window[nums[r]] = 1
                r += 1
            limit[l] = r - 1
            in_window[nums[l]] = 0
        freq = [0] * size
        req = [0] * size
        seen = [0] * size
        ans = 0
        for l in range(n):
            if limit[l] - l + 1 > K:
                ans += 1
                continue
            distinct = 0
            bad = 0
            mark = l + 1
            for r in range(l, n):
                v = nums[r]
                if seen[v] != mark:
                    seen[v] = mark
                    distinct += 1
                    if distinct > K:
                        break
                    if l + distinct * (distinct + 1) // 2 > n:
                        break
                    freq[v] = 1
                    req[v] = distinct
                    if distinct > 1:
                        bad += 1
                else:
                    c = freq[v] + 1
                    freq[v] = c
                    if c == req[v]:
                        bad -= 1
                    elif c > req[v]:
                        break
                if bad == 0:
                    ans += 1
        return ans
