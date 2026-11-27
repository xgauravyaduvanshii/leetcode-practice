# LeetCode 3357. Minimize the Maximum Adjacent Element Difference — Hard
# https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/
# Submission 2202421839 — Accepted, Python3
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # My thinking: binary-search the answer. For a candidate m, the only
        # pair worth trying is x = mn + m and y = mx - m, where mn/mx are
        # the smallest/largest known values next to a -1: x is the largest
        # value still within m of mn, y the smallest within m of mx, so any
        # gap a feasible pair could fill, this pair fills too. Each gap is
        # then checked on its own: a length-1 gap takes x or y, a longer gap
        # takes all x, all y, x-then-y or y-then-x, and an edge gap takes
        # whichever of x, y is nearer its known neighbour. Adjacent known
        # values bound the search from below.
        n = len(nums)
        if all(v == -1 for v in nums):
            return 0
        max_gap = 0
        mn = 10 ** 9 + 1
        mx = -1
        has_missing = False
        for i in range(n):
            if nums[i] == -1:
                has_missing = True
            if i > 0:
                a, b = nums[i - 1], nums[i]
                if a != -1 and b != -1:
                    max_gap = max(max_gap, abs(a - b))
                elif a == -1 and b != -1:
                    mn = min(mn, b)
                    mx = max(mx, b)
                elif a != -1 and b == -1:
                    mn = min(mn, a)
                    mx = max(mx, a)
        if not has_missing:
            return max_gap

        def check(m, x, y):
            i = 0
            while i < n:
                if nums[i] != -1:
                    i += 1
                    continue
                j = i
                while j < n and nums[j] == -1:
                    j += 1
                left = nums[i - 1] if i > 0 else None
                right = nums[j] if j < n else None
                if left is None and right is None:
                    pass
                elif left is None:
                    if min(abs(right - x), abs(right - y)) > m:
                        return False
                elif right is None:
                    if min(abs(left - x), abs(left - y)) > m:
                        return False
                elif j - i == 1:
                    if min(max(abs(left - x), abs(right - x)),
                           max(abs(left - y), abs(right - y))) > m:
                        return False
                else:
                    if min(max(abs(left - x), abs(x - right)),
                           max(abs(left - y), abs(y - right)),
                           max(abs(left - x), abs(x - y), abs(y - right)),
                           max(abs(left - y), abs(y - x), abs(x - right))) > m:
                        return False
                i = j
            return True

        lo, hi = max_gap, (mx - mn + 1) // 2
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid, mn + mid, mx - mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
