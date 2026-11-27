# LeetCode 3445. Maximum Difference Between Even and Odd Frequency II — Hard
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/
# Submission 2202540530 — Accepted 693/693, Python3
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        # My thinking: only the two digits a and b matter, so I try all
        # 20 pairs. For one pair, a substring's value is the difference
        # of the prefix counts (count_a - count_b), so I keep, for each
        # parity of the two counts, the smallest prefix difference seen
        # at a start that is far enough back: at least k behind, and no
        # later than the last b, so b appears at least twice in the
        # substring. The best end minus that minimum is the answer.
        n = len(s)
        INF = 10 ** 9
        ans = -INF
        for a in "01234":
            for b in "01234":
                if a == b:
                    continue
                pa = [0] * (n + 1)
                pb = [0] * (n + 1)
                for i, ch in enumerate(s):
                    pa[i + 1] = pa[i] + (ch == a)
                    pb[i + 1] = pb[i] + (ch == b)
                best = [[INF] * 2 for _ in range(2)]
                last_b = -1
                added = -1  # highest start index added so far
                for r in range(n + 1):
                    bound = min(r - k, last_b)
                    while added < bound:
                        added += 1
                        d = pa[added] - pb[added]
                        if d < best[pa[added] & 1][pb[added] & 1]:
                            best[pa[added] & 1][pb[added] & 1] = d
                    cur = best[1 - (pa[r] & 1)][pb[r] & 1]
                    if cur < INF:
                        val = (pa[r] - pb[r]) - cur
                        if val > ans:
                            ans = val
                    if r < n and s[r] == b:
                        last_b = r
        return ans
