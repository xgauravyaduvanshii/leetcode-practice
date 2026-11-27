# LeetCode 3398. Smallest Substring With Identical Characters I — Hard
# https://leetcode.com/problems/smallest-substring-with-identical-characters-i/
# Submission 2202506490 — Accepted 949/949, Python3
from collections import deque


class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        # My thinking: binary-search the answer L. For a fixed L,
        # the cheapest way to keep every run at most L long is a
        # left-to-right DP: the last run of the answer is one block
        # of equal characters, so the cost of ending at i with a
        # given character is the cost of that block plus the best
        # cost of the prefix before it ending in the other
        # character. The block cost is a difference of prefix
        # counts, so the best previous split is a sliding-window
        # minimum over the last L positions — two deques make the
        # whole check O(n).
        n = len(s)
        # nc0[i] / nc1[i]: number of '1's / '0's in s[:i].
        nc0 = [0] * (n + 1)
        nc1 = [0] * (n + 1)
        for i, ch in enumerate(s):
            nc0[i + 1] = nc0[i] + (ch == '1')
            nc1[i + 1] = nc1[i] + (ch == '0')

        def min_flips(limit: int) -> int:
            # v0[j + 1] = best cost of a prefix ending at j with a
            # '1', minus nc0[j + 1]; v1 is the mirror image.
            v0 = [0] * (n + 1)
            v1 = [0] * (n + 1)
            dq0 = deque([-1])
            dq1 = deque([-1])
            best0 = best1 = 0
            for i in range(n):
                while dq0[0] < i - limit:
                    dq0.popleft()
                while dq1[0] < i - limit:
                    dq1.popleft()
                best0 = nc0[i + 1] + v0[dq0[0] + 1]
                best1 = nc1[i + 1] + v1[dq1[0] + 1]
                v0[i + 1] = best1 - nc0[i + 1]
                v1[i + 1] = best0 - nc1[i + 1]
                while dq0 and v0[dq0[-1] + 1] >= v0[i + 1]:
                    dq0.pop()
                dq0.append(i)
                while dq1 and v1[dq1[-1] + 1] >= v1[i + 1]:
                    dq1.pop()
                dq1.append(i)
            return best0 if best0 < best1 else best1

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if min_flips(mid) <= numOps:
                hi = mid
            else:
                lo = mid + 1
        return lo
