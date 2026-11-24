# LeetCode 3501. Maximize Active Section with Trade II — Hard
# https://leetcode.com/problems/maximize-active-section-with-trade-ii/
# Submission 2202741807 — Accepted, Python3
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        # My thinking: the answer counts '1's in the whole string, so a
        # trade only adds the '0's it turns into '1's inside the queried
        # substring. A trade picks an interior '1'-block and turns the
        # two '0'-blocks next to it into '1's, gaining exactly those two
        # blocks' lengths (the '1'-block itself comes back). For a query
        # the gain of a '1'-block is the two neighbouring zero-runs cut
        # down to the query bounds. Only the first and the last interior
        # '1'-block can be cut at all: every middle block's runs lie
        # wholly inside the query, so its full value applies and the
        # best middle block is a range maximum over precomputed values.
        n = len(s)
        total_ones = s.count("1")
        blocks = []  # (start, end, left zero-run, right zero-run)
        i = 0
        while i < n:
            if s[i] == "1":
                j = i
                while j + 1 < n and s[j + 1] == "1":
                    j += 1
                lz = 0
                k = i - 1
                while k >= 0 and s[k] == "0":
                    lz += 1
                    k -= 1
                rz = 0
                k = j + 1
                while k < n and s[k] == "0":
                    rz += 1
                    k += 1
                blocks.append((i, j, lz, rz))
                i = j + 1
            else:
                i += 1
        if not blocks:
            return [total_ones] * len(queries)
        a_list = [b[0] for b in blocks]
        b_list = [b[1] for b in blocks]
        full = [b[2] + b[3] for b in blocks]
        m = len(blocks)
        LOG = [0] * (m + 1)
        for i in range(2, m + 1):
            LOG[i] = LOG[i // 2] + 1
        st = [full[:]]
        j = 1
        while (1 << j) <= m:
            prev = st[-1]
            cur = [0] * (m - (1 << j) + 1)
            for i in range(len(cur)):
                cur[i] = max(prev[i], prev[i + (1 << (j - 1))])
            st.append(cur)
            j += 1

        def range_max(l, r):
            if l > r:
                return 0
            j = LOG[r - l + 1]
            return max(st[j][l], st[j][r - (1 << j) + 1])

        ans = []
        for l, r in queries:
            first = bisect_right(a_list, l)
            last = bisect_left(b_list, r) - 1
            if first > last:
                ans.append(total_ones)
                continue
            gain = 0
            if first + 1 <= last - 1:
                gain = max(gain, range_max(first + 1, last - 1))
            a0, b0, lz0, rz0 = blocks[first]
            right0 = rz0 if first < last else min(rz0, r - b0)
            gain = max(gain, min(lz0, a0 - l) + right0)
            if last > first:
                a1, b1, lz1, rz1 = blocks[last]
                gain = max(gain, lz1 + min(rz1, r - b1))
            ans.append(total_ones + gain)
        return ans
