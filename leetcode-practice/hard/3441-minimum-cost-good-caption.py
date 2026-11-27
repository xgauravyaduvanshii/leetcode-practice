# LeetCode 3441. Minimum Cost Good Caption — Hard
# https://leetcode.com/problems/minimum-cost-good-caption/
# Submission 2202536622 — Accepted 714/714, Python3
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        # My thinking: a good caption is runs of one letter, each at least
        # 3 long, so I work backwards: for every position and every letter
        # the run ending just before it could have, I keep the cheapest
        # cost of finishing the rest. A new run may only start once the
        # previous run reached length 3. Then I walk forward, always taking
        # the smallest letter that can still reach the cheapest total —
        # that gives the lexicographically smallest cheapest caption.
        n = len(caption)
        if n < 3:
            return ""
        cap = [ord(ch) - 97 for ch in caption]
        INF = 10 ** 9
        # h1/h2/h3[i][c]: cheapest cost of caption[i:] when the run ending
        # at i-1 has letter c and length 1 / 2 / at least 3.
        h1 = [[INF] * 26 for _ in range(n + 1)]
        h2 = [[INF] * 26 for _ in range(n + 1)]
        h3 = [[0] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            ci = cap[i]
            A = [abs(ci - d) + h1[i + 1][d] for d in range(26)]
            b1 = b2 = INF
            c1 = -1
            for d in range(26):
                v = A[d]
                if v < b1:
                    b2, b1, c1 = b1, v, d
                elif v < b2:
                    b2 = v
            for c in range(26):
                cost = abs(ci - c)
                best_new = b1 if c1 != c else b2
                h3[i][c] = min(cost + h3[i + 1][c], best_new)
                h2[i][c] = cost + h3[i + 1][c]
                h1[i][c] = cost + h2[i + 1][c]
        total = min(abs(cap[0] - d) + h1[1][d] for d in range(26))
        res = []
        prev = -1  # letter of the run in progress, -1 = none yet
        run = 0    # its length, capped at 3
        remaining = total
        for i in range(n):
            ci = cap[i]
            for d in range(26):
                cost = abs(ci - d)
                if prev == -1:
                    value = cost + h1[i + 1][d]
                    new_run = 1
                elif d == prev:
                    nr = 3 if run == 3 else run + 1
                    nxt = h3 if nr == 3 else h2 if nr == 2 else h1
                    value = cost + nxt[i + 1][d]
                    new_run = nr
                elif run == 3:
                    value = cost + h1[i + 1][d]
                    new_run = 1
                else:
                    continue
                if value == remaining:
                    res.append(chr(d + 97))
                    remaining -= cost
                    prev, run = d, new_run
                    break
            else:
                raise AssertionError("no letter fits")
        return "".join(res)
