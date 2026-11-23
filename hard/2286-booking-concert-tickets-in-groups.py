# LeetCode 2286. Booking Concert Tickets in Groups — Hard
# https://leetcode.com/problems/booking-concert-tickets-in-groups/
# Submission 2201656814 — Accepted, Python3
#
# My thinking: every row keeps its empty
# stretches in order, and a segment tree
# over the rows finds the first row with
# room — gather takes one solid block,
# scatter fills the smallest rows first.

import bisect


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.empty = [[[0, m - 1]] for _ in range(n)]
        size = 1
        while size < n:
            size *= 2
        self.size = size
        self.tree_max = [0] * (2 * size)
        self.tree_sum = [0] * (2 * size)
        for i in range(n):
            self.tree_max[size + i] = m
            self.tree_sum[size + i] = m
        for i in range(size - 1, 0, -1):
            self.tree_max[i] = max(self.tree_max[2 * i], self.tree_max[2 * i + 1])
            self.tree_sum[i] = self.tree_sum[2 * i] + self.tree_sum[2 * i + 1]

    def _row_stats(self, r: int):
        ivs = self.empty[r]
        total = 0
        best = 0
        for l, rr in ivs:
            total += rr - l + 1
            if rr - l + 1 > best:
                best = rr - l + 1
        return best, total

    def _update_row(self, r: int):
        best, total = self._row_stats(r)
        i = self.size + r
        self.tree_max[i] = best
        self.tree_sum[i] = total
        i //= 2
        while i:
            self.tree_max[i] = max(self.tree_max[2 * i], self.tree_max[2 * i + 1])
            self.tree_sum[i] = self.tree_sum[2 * i] + self.tree_sum[2 * i + 1]
            i //= 2

    def _range_sum(self, l: int, r: int) -> int:
        l += self.size
        r += self.size
        s = 0
        while l <= r:
            if l % 2 == 1:
                s += self.tree_sum[l]
                l += 1
            if r % 2 == 0:
                s += self.tree_sum[r]
                r -= 1
            l //= 2
            r //= 2
        return s

    def _first_row_with(self, k: int, max_row: int) -> int:
        if self.tree_max[1] < k:
            return -1
        i = 1
        l, r = 0, self.size - 1
        while i < self.size:
            left = 2 * i
            mid = (l + r) // 2
            if self.tree_max[left] >= k and l <= max_row:
                i = left
                r = mid
            else:
                i = left + 1
                l = mid + 1
        row = i - self.size
        if row > max_row or row >= self.n:
            return -1
        return row

    def _take_from_row(self, r: int, k: int) -> int:
        ivs = self.empty[r]
        taken = 0
        while k > 0 and ivs:
            l, rr = ivs[0]
            length = rr - l + 1
            take = min(length, k)
            taken += take
            k -= take
            if take == length:
                ivs.pop(0)
            else:
                ivs[0][0] = l + take
        return taken

    def gather(self, k: int, maxRow: int) -> list[int]:
        r = self._first_row_with(k, maxRow)
        if r == -1:
            return []
        ivs = self.empty[r]
        c = -1
        for idx, (l, rr) in enumerate(ivs):
            if rr - l + 1 >= k:
                c = l
                if rr - l + 1 == k:
                    ivs.pop(idx)
                else:
                    ivs[idx][0] = l + k
                break
        if c == -1:
            return []
        self._update_row(r)
        return [r, c]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self._range_sum(0, maxRow) < k:
            return False
        r = 0
        while k > 0:
            while r <= maxRow and self.tree_sum[self.size + r] == 0:
                r += 1
            if r > maxRow:
                return False
            taken = self._take_from_row(r, k)
            k -= taken
            self._update_row(r)
            if k > 0:
                r += 1
        return True
