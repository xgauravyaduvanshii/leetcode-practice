# LeetCode 3826. Minimum Partition Score — Hard
# https://leetcode.com/problems/minimum-partition-score/
# Submission 2203197630 — Accepted, Python3
from typing import List


class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        # My thinking: prefix sums P turn a piece's value into
        # S(S+1)/2 where S is a difference of two prefix sums,
        # so dp[t][i] — the best score of splitting the first
        # i numbers into t pieces — is (P[i]^2+P[i])/2 plus
        # the minimum over split points j of dp[t-1][j] +
        # (P[j]^2-P[j])/2 - P[i]*P[j]. For fixed j that is a
        # line in x = P[i] with slope -P[j] and intercept
        # dp[t-1][j] + (P[j]^2-P[j])/2. The numbers are
        # positive, so the prefix sums — and the query points
        # — strictly increase while the slopes strictly
        # decrease, which is exactly the monotone convex hull
        # trick: a deque holds the lower hull, lines are
        # dropped from the back when a new line makes them
        # useless (integer cross-multiplication, no floats)
        # and from the front once the next line beats them at
        # the current query point. Each layer costs O(n).
        n = len(nums)
        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x
        INF = float("inf")
        prev = [INF] * (n + 1)
        prev[0] = 0
        for t in range(1, k + 1):
            cur = [INF] * (n + 1)
            # Deque of (slope, intercept) lines, slopes
            # strictly decreasing; head is the first live line.
            hull = []
            head = 0
            for i in range(t, n + 1):
                j = i - 1
                # Add the line for split point j, if j can be
                # split into t-1 pieces at all.
                if prev[j] < INF:
                    m = -pref[j]
                    b = prev[j] + (pref[j] * pref[j] - pref[j]) // 2
                    while len(hull) - head >= 2:
                        m1, b1 = hull[-2]
                        m2, b2 = hull[-1]
                        # The middle line is useless exactly
                        # when its crossing with the first line
                        # is at or after its crossing with the
                        # new line: (b2-b1)/(m1-m2) >=
                        # (b-b2)/(m2-m), cross-multiplied (both
                        # denominators are positive).
                        if (b2 - b1) * (m2 - m) >= (b - b2) * (m1 - m2):
                            hull.pop()
                        else:
                            break
                    hull.append((m, b))
                if len(hull) - head == 0:
                    continue
                x = pref[i]
                while len(hull) - head >= 2:
                    m1, b1 = hull[head]
                    m2, b2 = hull[head + 1]
                    if m1 * x + b1 >= m2 * x + b2:
                        head += 1
                    else:
                        break
                m, b = hull[head]
                cur[i] = (pref[i] * pref[i] + pref[i]) // 2 + m * x + b
            prev = cur
        return prev[n]
