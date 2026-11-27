# LeetCode 3245. Alternating Groups III — Hard
# https://leetcode.com/problems/alternating-groups-iii/
# Submission 2202132772 — Accepted, Python3
#
# My thinking: positions where neighbours are
# equal ("bad" edges) split the circle into
# alternating blocks. A block of length L holds
# max(0, L - k + 1) alternating groups of size
# k. I keep the bad edges sorted and two Fenwick
# trees over block lengths (count and sum), so
# a colour flip only touches the two blocks next
# to it and every query is O(log n).

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        from bisect import bisect_left
        n = len(colors)
        bit_c = [0] * (n + 2)
        bit_s = [0] * (n + 2)

        def block_add(length, delta):
            i = length
            while i <= n:
                bit_c[i] += delta
                i += i & -i
            i = length
            add = delta * length
            while i <= n:
                bit_s[i] += add
                i += i & -i

        def prefix(bit, idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s

        def dist(a, b):
            d = b - a
            if d <= 0:
                d += n
            return d

        bads = []
        for i in range(n):
            if colors[i] == colors[(i + 1) % n]:
                bads.append(i)
        m = len(bads)
        for j in range(m):
            block_add(dist(bads[j], bads[(j + 1) % m]), 1)

        def add_bad(e):
            if not bads:
                block_add(n, 1)
                bads.append(e)
                return
            i = bisect_left(bads, e)
            pred = bads[i - 1] if i > 0 else bads[-1]
            succ = bads[i] if i < len(bads) else bads[0]
            block_add(dist(pred, succ), -1)
            block_add(dist(pred, e), 1)
            block_add(dist(e, succ), 1)
            bads.insert(i, e)

        def remove_bad(e):
            if len(bads) == 1:
                block_add(n, -1)
                del bads[0]
                return
            i = bisect_left(bads, e)
            pred = bads[i - 1] if i > 0 else bads[-1]
            succ = bads[i + 1] if i + 1 < len(bads) else bads[0]
            block_add(dist(pred, e), -1)
            block_add(dist(e, succ), -1)
            block_add(dist(pred, succ), 1)
            del bads[i]

        ans = []
        for q in queries:
            if q[0] == 1:
                k = q[1]
                if not bads:
                    ans.append(n)
                else:
                    cnt_ge = len(bads) - prefix(bit_c, k - 1)
                    sum_ge = n - prefix(bit_s, k - 1)
                    ans.append(sum_ge - (k - 1) * cnt_ge)
            else:
                idx = q[1]
                col = q[2]
                if colors[idx] == col:
                    continue
                prev = colors[(idx - 1) % n]
                nxt = colors[(idx + 1) % n]
                old = colors[idx]
                e1 = (idx - 1) % n
                e2 = idx
                was1 = prev == old
                now1 = prev == col
                was2 = old == nxt
                now2 = col == nxt
                colors[idx] = col
                if was1 != now1:
                    if now1:
                        add_bad(e1)
                    else:
                        remove_bad(e1)
                if was2 != now2:
                    if now2:
                        add_bad(e2)
                    else:
                        remove_bad(e2)
        return ans
