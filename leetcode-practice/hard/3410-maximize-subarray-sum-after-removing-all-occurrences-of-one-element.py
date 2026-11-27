# LeetCode 3410. Maximize Subarray Sum After Removing All Occurrences of One Element — Hard
# https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/
# Submission 2202513821 — Accepted 660/660, Python3
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        # My thinking: deleting all of one value x cuts the array
        # into blocks of non-x elements, and any best subarray of
        # what is left either sits inside one block — then plain
        # Kadane on the original array already covers it — or spans
        # several blocks, in which case it is a suffix of the first
        # block, whole blocks in the middle, and a prefix of the
        # last block. A sparse table over the prefix sums gives each
        # block's best prefix and suffix in O(1), so one sweep per
        # value finds its best spanning subarray; the total work
        # over all values is O(n log n).
        n = len(nums)
        pref = [0] * (n + 1)
        for i, v in enumerate(nums):
            pref[i + 1] = pref[i] + v

        # Best subarray sum with no deletion (plain Kadane).
        cur = best = nums[0]
        for v in nums[1:]:
            cur = v if cur < 0 else cur + v
            if cur > best:
                best = cur
        ans = best

        # Sparse tables for range min / max of the prefix sums.
        size = n + 1
        logs = [0] * (size + 1)
        for i in range(2, size + 1):
            logs[i] = logs[i // 2] + 1
        st_min = [pref]
        st_max = [pref]
        j = 1
        while (1 << j) <= size:
            step = 1 << (j - 1)
            prev_min = st_min[-1]
            st_min.append([a if a < b else b
                           for a, b in zip(prev_min, prev_min[step:])])
            prev_max = st_max[-1]
            st_max.append([a if a > b else b
                           for a, b in zip(prev_max, prev_max[step:])])
            j += 1

        def range_min(lo: int, hi: int) -> int:
            k = logs[hi - lo + 1]
            a = st_min[k][lo]
            b = st_min[k][hi - (1 << k) + 1]
            return a if a < b else b

        def range_max(lo: int, hi: int) -> int:
            k = logs[hi - lo + 1]
            a = st_max[k][lo]
            b = st_max[k][hi - (1 << k) + 1]
            return a if a > b else b

        positions = {}
        for i, v in enumerate(nums):
            positions.setdefault(v, []).append(i)

        for pos in positions.values():
            # Blocks are the stretches between consecutive
            # occurrences of this value (and the two ends).
            total = 0  # sum of the block sums seen so far
            best_u = None  # best (max suffix - block sums so far)
            prev = -1
            for p in pos + [n]:
                a, b = prev + 1, p - 1
                if a <= b:
                    block_sum = pref[b + 1] - pref[a]
                    # Best suffix of this block: pref[b + 1] minus
                    # the smallest prefix sum inside the block.
                    suffix = pref[b + 1] - range_min(a, b)
                    # Best prefix of this block: largest prefix sum
                    # just past the block minus pref[a].
                    prefix = range_max(a + 1, b + 1) - pref[a]
                    if best_u is not None:
                        cand = total + prefix + best_u
                        if cand > ans:
                            ans = cand
                    total += block_sum
                    val = suffix - total
                    if best_u is None or val > best_u:
                        best_u = val
                prev = p
        return ans
