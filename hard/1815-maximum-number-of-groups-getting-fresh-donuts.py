# LeetCode 1815. Maximum Number of Groups Getting Fresh Donuts — Hard
# https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/
# Submission 2201180551 — Accepted, Python3
#
# My thinking: groups with no remainder are always
# fresh, and complementary remainders pair up into
# fresh groups on their own — whatever is left I
# order by trying every next remainder and keeping
# the running total modulo the batch size.

from collections import Counter
from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: list[int]) -> int:
        cnt = Counter(g % batchSize for g in groups)
        ans = cnt[0]
        del cnt[0]
        for r in range(1, batchSize):
            if cnt.get(r, 0) == 0:
                continue
            comp = batchSize - r
            if r == comp:
                ans += cnt[r] // 2
                cnt[r] %= 2
            elif r < comp:
                pairs = min(cnt[r], cnt.get(comp, 0))
                ans += pairs
                cnt[r] -= pairs
                cnt[comp] -= pairs
        remainders = [r for r in range(1, batchSize) if cnt.get(r, 0) > 0]
        init = tuple(cnt.get(r, 0) for r in remainders)

        @lru_cache(None)
        def dp(state, cur):
            best = 0
            for idx, r in enumerate(remainders):
                if state[idx] == 0:
                    continue
                lst = list(state)
                lst[idx] -= 1
                ncur = (cur + r) % batchSize
                gain = 1 if ncur == 0 else 0
                best = max(best, gain + dp(tuple(lst), ncur))
            return best

        return ans + dp(init, 0)
