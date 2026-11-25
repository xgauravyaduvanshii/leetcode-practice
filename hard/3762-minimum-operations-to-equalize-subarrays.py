# LeetCode 3762. Minimum Operations to Equalize Subarrays — Hard
# https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/
# Submission 2203162555 — Accepted, Python3
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        # My thinking: changing an element by steps of k can
        # only reach values in its own residue class mod k, so
        # a query is impossible when its range mixes residues
        # — a prefix count of residue changes spots that in
        # O(1). Otherwise every value in the range shares one
        # residue, and the cheapest target is a median of the
        # range: the cost is the sum of absolute deviations
        # from the median, divided by k. A persistent segment
        # tree over the compressed values gives, for any range,
        # its median by rank and the count and sum of values
        # below it, so each query costs O(log n) after one
        # O(n log n) build.
        n = len(nums)
        vals = sorted(set(nums))
        comp = {v: i for i, v in enumerate(vals)}
        m = len(vals)
        left = [0]
        right = [0]
        cnt = [0]
        ssum = [0]

        def update(prev: int, l: int, r: int, pos: int, val: int) -> int:
            idx = len(cnt)
            cnt.append(cnt[prev] + 1)
            ssum.append(ssum[prev] + val)
            left.append(0)
            right.append(0)
            if l != r:
                mid = (l + r) // 2
                if pos <= mid:
                    left[idx] = update(left[prev], l, mid, pos, val)
                    right[idx] = right[prev]
                else:
                    left[idx] = left[prev]
                    right[idx] = update(right[prev], mid + 1, r, pos, val)
            return idx

        roots = [0] * (n + 1)
        for i, v in enumerate(nums):
            roots[i + 1] = update(roots[i], 0, m - 1, comp[v], v)

        def kth(node_r: int, node_l: int, l: int, r: int, rank: int) -> int:
            while l != r:
                mid = (l + r) // 2
                c = cnt[left[node_r]] - cnt[left[node_l]]
                if rank <= c:
                    node_r = left[node_r]
                    node_l = left[node_l]
                    r = mid
                else:
                    rank -= c
                    node_r = right[node_r]
                    node_l = right[node_l]
                    l = mid + 1
            return l

        def prefix(node_r: int, node_l: int, l: int, r: int, qr: int):
            if qr < l:
                return (0, 0)
            if r <= qr:
                return (cnt[node_r] - cnt[node_l], ssum[node_r] - ssum[node_l])
            mid = (l + r) // 2
            c1, s1 = prefix(left[node_r], left[node_l], l, mid, qr)
            c2, s2 = prefix(right[node_r], right[node_l], mid + 1, r, qr)
            return (c1 + c2, s1 + s2)

        pref_sum = [0] * (n + 1)
        for i, v in enumerate(nums):
            pref_sum[i + 1] = pref_sum[i] + v
        bad = [0] * (n + 1)
        for i in range(1, n):
            bad[i + 1] = bad[i] + (1 if nums[i] % k != nums[i - 1] % k else 0)
        # bad[i] counts residue changes among indices < i, so
        # the changes inside [l, r] are bad[r + 1] - bad[l + 1].
        ans = []
        for l, r in queries:
            if bad[r + 1] - bad[l + 1] > 0:
                ans.append(-1)
                continue
            length = r - l + 1
            mi = kth(roots[r + 1], roots[l], 0, m - 1, (length + 1) // 2)
            med = vals[mi]
            cnt_le, sum_le = prefix(roots[r + 1], roots[l], 0, m - 1, mi)
            cnt_gt = length - cnt_le
            sum_gt = (pref_sum[r + 1] - pref_sum[l]) - sum_le
            cost = med * cnt_le - sum_le + sum_gt - med * cnt_gt
            ans.append(cost // k)
        return ans
