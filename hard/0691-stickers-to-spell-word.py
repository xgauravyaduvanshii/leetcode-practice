# LeetCode 691. Stickers to Spell Word — Hard
# https://leetcode.com/problems/stickers-to-spell-word/
# Submission 2198668050 — Accepted, Python3
#
# My thinking: I track which letters of the target are
# still missing as a bitmask. For the first missing
# letter I try every sticker that has it, peel off
# every letter that sticker covers, and take the best
# of the rest — memoised, so each mask is solved once.

from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        counts = [Counter(s) for s in stickers]

        @lru_cache(None)
        def best(mask):
            if mask == 0:
                return 0
            first = next(i for i in range(n) if mask >> i & 1)
            answer = float("inf")
            for sticker in counts:
                if sticker[target[first]] == 0:
                    continue
                remaining = sticker.copy()
                new_mask = mask
                for j in range(n):
                    if new_mask >> j & 1 and remaining[target[j]] > 0:
                        remaining[target[j]] -= 1
                        new_mask &= ~(1 << j)
                if new_mask != mask:
                    answer = min(answer, 1 + best(new_mask))
            return answer

        result = best((1 << n) - 1)
        return -1 if result == float("inf") else result
