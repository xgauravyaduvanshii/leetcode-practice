# LeetCode 4017. Peaks in Array II — Hard
# https://leetcode.com/problems/peaks-in-array-ii/
# Submission 2203512837 — Accepted, Python3
from typing import List
from bisect import bisect_left, bisect_right, insort


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # My thinking: a subarray is a peak subarray when
        # it holds a peak strictly inside it. Split the
        # query range [l, r] at its peaks p1 < ... < pm
        # (with p0 = l and p(m+1) = r as boundaries): a
        # subarray of length at least 3 has no peak inside
        # exactly when both ends fall in one gap between
        # consecutive boundaries, and gap t of length g
        # holds C(g, 2) such subarrays. So the answer is
        # C(r-l+1, 2) - (r-l) - sum C(g, 2) over the gaps,
        # which simplifies to ((r-l)^2 - sum g^2) / 2.
        # Expanding sum g^2 over the gaps and telescoping
        # the peak products gives r*(b-l) - W + a*(l-q),
        # where a = p1 is the first peak in (l, r),
        # b = pm is the last peak, q is the peak just
        # before a (0 if there is none), and W is the sum
        # of p*(p - prev(p)) over the peaks in (l, r),
        # with prev(p) the previous peak in the whole
        # array (0 if there is none). A Fenwick tree holds
        # those p*(p - prev(p)) values, and a sorted list
        # holds the peaks, so a query reads a, b, q and W
        # in O(log n). An update only changes peak status
        # at i-1, i, i+1 and the value of the next peak
        # after each of those, so refresh exactly those.
        n = len(nums)

        def is_peak(k: int) -> bool:
            return 0 < k < n - 1 and nums[k] > nums[k - 1] and nums[k] > nums[k + 1]

        peaks = [k for k in range(1, n - 1) if is_peak(k)]
        bit = [0] * (n + 2)

        def bit_add(i: int, d: int) -> None:
            i += 1
            while i <= n + 1:
                bit[i] += d
                i += i & -i

        def bit_sum(i: int) -> int:
            total = 0
            while i:
                total += bit[i]
                i -= i & -i
            return total

        def peak_value(p: int) -> int:
            idx = bisect_left(peaks, p)
            prev = peaks[idx - 1] if idx > 0 else 0
            return p * (p - prev)

        for p in peaks:
            bit_add(p, peak_value(p))

        def has_peak(p: int) -> bool:
            idx = bisect_left(peaks, p)
            return idx < len(peaks) and peaks[idx] == p

        ans = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                lo = bisect_right(peaks, l)
                hi = bisect_left(peaks, r)
                if lo == hi:
                    ans.append(0)
                    continue
                a = peaks[lo]
                b = peaks[hi - 1]
                prev_a = peaks[lo - 1] if lo > 0 else 0
                w = bit_sum(b + 1) - bit_sum(a)
                ans.append(r * (b - l) - w + a * (l - prev_a))
            else:
                i, val = q[1], q[2]
                refresh = set()
                for k in (i - 1, i, i + 1):
                    if 1 <= k <= n - 2:
                        refresh.add(k)
                        j = bisect_right(peaks, k)
                        if j < len(peaks):
                            refresh.add(peaks[j])
                for p in refresh:
                    if has_peak(p):
                        bit_add(p, -peak_value(p))
                for k in (i - 1, i, i + 1):
                    if 1 <= k <= n - 2:
                        if has_peak(k):
                            idx = bisect_left(peaks, k)
                            del peaks[idx]
                nums[i] = val
                for k in (i - 1, i, i + 1):
                    if 1 <= k <= n - 2 and is_peak(k):
                        insort(peaks, k)
                for p in refresh:
                    if has_peak(p):
                        bit_add(p, peak_value(p))
        return ans
