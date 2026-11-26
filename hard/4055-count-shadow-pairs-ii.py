# LeetCode 4055. Count Shadow Pairs II — Hard
# https://leetcode.com/problems/count-shadow-pairs-ii/
# Submission 2203579876 — Accepted, Python3
from bisect import bisect_left, bisect_right, insort
from typing import List


class Solution:
    def shadowPairs(self, nums: List[int]) -> int:
        # My thinking: split the array in half and count
        # cross pairs, then recurse. For i on the left let
        # b[i] be the smallest value after i in the left
        # half that is bigger than nums[i] (or infinity);
        # for j on the right let c[j] be the largest value
        # before j in the right half that is smaller than
        # nums[j] (or zero). A cross pair is a shadow pair
        # exactly when nums[i] < nums[j], b[i] >= nums[j]
        # and c[j] <= nums[i]. Sweeping j by rising value
        # with a Fenwick tree over the left values counts
        # those i's, adding each i when it becomes eligible
        # and dropping it once its b[i] bound is passed.
        INF = 2_000_000_000
        a = nums
        n = len(a)

        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, idx, delta):  # 0-based idx
                bit = self.bit
                n = self.n
                idx += 1
                while idx <= n:
                    bit[idx] += delta
                    idx += idx & -idx

            def sum_prefix(self, idx):  # sum of [0, idx)
                s = 0
                bit = self.bit
                while idx > 0:
                    s += bit[idx]
                    idx -= idx & -idx
                return s

            def range_sum(self, l, r):
                return self.sum_prefix(r) - self.sum_prefix(l)

        def solve(l, r):
            if r - l <= 1:
                return 0
            m = (l + r) // 2
            ans = solve(l, m) + solve(m, r)

            # b[i] for i in [l, m): successor of a[i] among
            # values to its right in the half.
            b = [INF] * (m - l)
            seen = []
            for i in range(m - 1, l - 1, -1):
                j = bisect_right(seen, a[i])
                if j < len(seen):
                    b[i - l] = seen[j]
                insort(seen, a[i])
            # c[j] for j in [m, r): predecessor of a[j]
            # among values to its left in the half.
            c = [0] * (r - m)
            seen = []
            for j in range(m, r):
                k = bisect_left(seen, a[j])
                if k > 0:
                    c[j - m] = seen[k - 1]
                insort(seen, a[j])

            # Left indices sorted by value, and by b bound.
            L = sorted(range(m - l), key=lambda i: a[l + i])
            Lb = sorted(range(m - l), key=lambda i: b[i])
            R = sorted(range(r - m), key=lambda j: a[m + j])

            # Coordinate-compress the left values for the
            # Fenwick tree.
            comp = sorted(set(a[l:m]))
            ft = Fenwick(len(comp))

            added = [False] * (m - l)
            p = q = 0
            for jj in R:
                vj = a[m + jj]
                while p < len(L) and a[l + L[p]] < vj:
                    i = L[p]
                    if b[i] >= vj:
                        ft.add(bisect_left(comp, a[l + i]), 1)
                        added[i] = True
                    p += 1
                while q < len(Lb) and b[Lb[q]] < vj:
                    i = Lb[q]
                    if added[i]:
                        ft.add(bisect_left(comp, a[l + i]), -1)
                        added[i] = False
                    q += 1
                lo = bisect_left(comp, c[jj])
                ans += ft.range_sum(lo, len(comp))
            return ans

        return solve(0, n)
