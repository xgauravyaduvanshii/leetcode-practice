# LeetCode 3414. Maximum Score of Non-overlapping Intervals — Hard
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/
# Submission 2202517080 — Accepted 581/581, Python3
from typing import List
import bisect


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # My thinking: sort the intervals by start, so the first
        # interval after i that starts past i's end is a binary
        # search away. Then work backwards: from position i with k
        # picks left, either skip i or take it and continue from
        # that next position with k - 1 picks. Keep, for every state,
        # the best weight and — on a tie — the lexicographically
        # smallest sorted list of original indices, which is what
        # the problem asks for.
        n = len(intervals)
        arr = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        lefts = [a[0] for a in arr]
        nxt = [bisect.bisect_right(lefts, arr[i][1]) for i in range(n)]

        # f[i][k] = (best weight, sorted index tuple) using intervals
        # from position i onward with at most k picks.
        f = [[(0, ())] * 5 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            _, _, w, idx = arr[i]
            j = nxt[i]
            for k in range(1, 5):
                skip = f[i + 1][k]
                take_w, take_t = f[j][k - 1]
                take = (w + take_w, tuple(sorted(take_t + (idx,))))
                if take[0] > skip[0] or (take[0] == skip[0] and take[1] < skip[1]):
                    f[i][k] = take
                else:
                    f[i][k] = skip
        return list(f[0][4][1])
