# LeetCode 2659. Make Array Empty — Hard
# https://leetcode.com/problems/make-array-empty/
# Submission 2201861748 — Accepted, Python3
#
# My thinking: the numbers leave in
# increasing order, so for each one I
# count how many are still standing
# between the front of the line and it
# — those all have to step aside first,
# and a Fenwick tree keeps the count
# honest as the line thins out.

class Solution:
    def countOperationsToEmptyArray(self, nums: list[int]) -> int:
        n = len(nums)
        pos = {v: i for i, v in enumerate(nums)}
        # Fenwick tree over "still present" (1) / removed (0)
        bit = [0] * (n + 1)

        def bit_add(i, delta):
            i += 1
            while i <= n:
                bit[i] += delta
                i += i & -i

        def bit_sum(i):
            # sum of [0, i]
            if i < 0:
                return 0
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        for i in range(n):
            bit_add(i, 1)
        front = 0
        ops = 0
        for v in sorted(nums):
            p = pos[v]
            if p >= front:
                before = bit_sum(p - 1) - bit_sum(front - 1)
            else:
                before = bit_sum(n - 1) - bit_sum(front - 1) + bit_sum(p - 1)
            ops += before + 1
            bit_add(p, -1)
            # new front: the next alive element after p (wrapping around)
            if bit_sum(n - 1) == 0:
                break
            if bit_sum(n - 1) - bit_sum(p) > 0:
                # find the smallest alive index > p
                lo, hi = p + 1, n - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if bit_sum(mid) - bit_sum(p) > 0:
                        hi = mid
                    else:
                        lo = mid + 1
                front = lo
            else:
                lo, hi = 0, n - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if bit_sum(mid) > 0:
                        hi = mid
                    else:
                        lo = mid + 1
                front = lo
        return ops
