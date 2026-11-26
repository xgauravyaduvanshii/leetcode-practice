# LeetCode 4007. Widest Possible Fence — Hard
# https://leetcode.com/problems/widest-possible-fence/
# Submission 2203506312 — Accepted, Python3
from typing import List
from collections import Counter


class Solution:
    def maximumWidth(self, planks: List[int]) -> int:
        # My thinking: for a target height h, the fence can
        # use every plank of height h as is, plus disjoint
        # pairs of planks that add up to h. A pair summing
        # to h uses two planks both shorter than h, so the
        # singles and the pairs never compete for planks,
        # and pairs of different value splits (v, h-v) never
        # share a plank either. So for each h the best count
        # is freq[h] plus, over every value split, the pairs
        # that split can supply: min(freq[v], freq[h-v]) for
        # v < h-v, and freq[v] // 2 for v == h-v. Instead of
        # scoring every h from scratch, group by pair sum:
        # each pair of distinct values (v, w) contributes
        # min(freq[v], freq[w]) pairs to the sum v + w, and
        # each value contributes freq[v] // 2 pairs to 2v.
        # Then the answer is the best freq[h] + pairs[h]
        # over all heights and pair sums. A single plank
        # alone always works, so the answer is at least 1.
        freq = Counter(planks)
        vals = sorted(freq)
        pairs = Counter()
        for i, v in enumerate(vals):
            pairs[2 * v] += freq[v] // 2
            for w in vals[i + 1:]:
                pairs[v + w] += min(freq[v], freq[w])
        ans = 1
        for h in set(freq) | set(pairs):
            ans = max(ans, freq.get(h, 0) + pairs.get(h, 0))
        return ans
