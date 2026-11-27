# LeetCode 1982. Find Array Given Subset Sums — Hard
# https://leetcode.com/problems/find-array-given-subset-sums/
# Submission 2201287613 — Accepted, Python3
#
# My thinking: the biggest gap between the two
# largest subset sums is the smallest element by
# size, so I peel elements off one at a time —
# a sign only counts if the sums left behind
# still hold 0 and the right ends.

from collections import Counter

class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        def try_remove(cnt, a):
            # Split the subset sums into those without a and those with a.
            # Returns the Counter of the sums without a, or None if a does not fit.
            cnt = Counter(cnt)
            rest = Counter()
            if a > 0:
                keys = sorted(cnt)
            else:
                keys = sorted(cnt, reverse=True)
            for s in keys:
                while cnt[s] > 0:
                    if cnt[s + a] <= 0:
                        return None
                    cnt[s] -= 1
                    cnt[s + a] -= 1
                    rest[s] += 1
            return rest

        cnt = Counter(sums)
        ans = []
        for _ in range(n):
            keys = sorted(k for k, v in cnt.items() if v > 0)
            if len(keys) == 1:
                # Every subset sum is the same, so the rest are all zeroes.
                ans.extend([0] * (n - len(ans)))
                break
            m = keys[-1] - keys[-2]
            lo, hi = keys[0], keys[-1]
            rest = try_remove(cnt, m)
            if rest is not None and rest.get(0, 0) > 0:
                rkeys = sorted(k for k, v in rest.items() if v > 0)
                if rkeys and rkeys[0] == lo and rkeys[-1] == hi - m:
                    ans.append(m)
                    cnt = rest
                    continue
            rest = try_remove(cnt, -m)
            if rest is not None and rest.get(0, 0) > 0:
                rkeys = sorted(k for k, v in rest.items() if v > 0)
                if rkeys and rkeys[0] == lo + m and rkeys[-1] == hi:
                    ans.append(-m)
                    cnt = rest
                    continue
            raise ValueError("no consistent split")
        return ans
