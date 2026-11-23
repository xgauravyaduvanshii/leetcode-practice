# LeetCode 2468. Split Message Based on Limit — Hard
# https://leetcode.com/problems/split-message-based-on-limit/
# Submission 2201765525 — Accepted, Python3
#
# My thinking: the suffix "<a/b>" eats a
# different number of characters depending
# on how many digits a and b have, so I
# try the smallest part-count first and
# add up exactly what each part can hold
# — the first count whose parts swallow
# the whole message is the answer.

class Solution:
    def splitMessage(self, message: str, limit: int) -> list[str]:
        n = len(message)

        def suffix_len(a, b):
            return 3 + len(str(a)) + len(str(b))

        for b in range(1, n + 1):
            capacities = []
            ok = True
            for a in range(1, b + 1):
                cap = limit - suffix_len(a, b)
                if cap <= 0:
                    ok = False
                    break
                capacities.append(cap)
            if not ok:
                continue
            if sum(capacities) < n:
                continue
            parts = []
            idx = 0
            for a in range(1, b + 1):
                take = min(capacities[a - 1], n - idx)
                parts.append(message[idx:idx + take] + f"<{a}/{b}>")
                idx += take
            if idx == n:
                return parts
        return []
