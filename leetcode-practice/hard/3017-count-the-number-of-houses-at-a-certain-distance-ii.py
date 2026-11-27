# LeetCode 3017. Count the Number of Houses at a Certain Distance II — Hard
# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/
# Submission 2201885397 — Accepted, Python3
#
# My thinking: the extra street turns
# the houses from x to y into a cycle,
# with a plain line hanging off each
# end. I count the pairs inside each
# part on its own — lines by length,
# the cycle by going either way round
# — and the pairs across parts by how
# far each house sits from the end it
# hangs off, adding whole ranges at a
# time with a difference array.

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if x == y:
            # No shortcut at all: a plain line of n houses.
            return [2 * (n - d) if d < n else 0 for d in range(1, n + 1)]
        if x > y:
            x, y = y, x
        d = y - x
        left_len = x - 1
        right_len = n - y
        m = d + 1  # houses on the cycle, x..y
        ans = [0] * (n + 1)  # ans[t] = unordered pairs at distance t

        # Pairs inside the left line and inside the right line.
        for t in range(1, left_len):
            ans[t] += left_len - t
        for t in range(1, right_len):
            ans[t] += right_len - t

        # Pairs inside the cycle: each house has two at every distance
        # below half the cycle, one at exactly half when the cycle is even.
        for t in range(1, (m - 1) // 2 + 1):
            ans[t] += m
        if m % 2 == 0:
            ans[m // 2] += m // 2

        # How many cycle houses sit at each cycle-distance from an end.
        cnt_c = [0] * (m // 2 + 2)
        for j in range(m):
            cnt_c[min(j, m - j)] += 1

        # Difference array for the cross-part range additions.
        diff = [0] * (n + 3)

        def range_add(lo: int, hi: int, val: int) -> None:
            if val == 0 or lo > hi:
                return
            lo = max(lo, 1)
            hi = min(hi, n)
            if lo > hi:
                return
            diff[lo] += val
            diff[hi + 1] -= val

        # Left line to cycle, and right line to cycle: a house i steps
        # from the end plus a cycle house v steps round the cycle.
        for v, c in enumerate(cnt_c):
            if c:
                range_add(v + 1, v + left_len, c)
                range_add(v + 1, v + right_len, c)
        # Left line to right line: i steps out one side, j out the other,
        # one street across the shortcut.
        for i in range(1, left_len + 1):
            range_add(i + 2, i + right_len + 1, 1)

        run = 0
        for t in range(1, n + 1):
            run += diff[t]
            ans[t] += run
        # Every unordered pair is two ordered pairs.
        return [2 * ans[t] for t in range(1, n + 1)]
