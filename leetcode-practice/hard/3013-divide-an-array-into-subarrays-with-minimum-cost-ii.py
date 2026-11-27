# LeetCode 3013. Divide an Array Into Subarrays With Minimum Cost II — Hard
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
# Submission 2201883226 — Accepted, Python3
#
# My thinking: the first piece always
# costs nums[0], so I only have to pick
# the other k - 1 cut spots. They must
# all sit inside a window of length
# dist, so I slide that window along
# and keep the cheapest k - 1 values in
# it with two heaps — the small ones I
# picked, and the rest waiting to swap
# in.

import heapq


class Solution:
    def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
        n = len(nums)
        need = k - 1
        # small: max-heap (negated) of the `need` cheapest live values in
        # the window, with their running sum. large: min-heap of the rest.
        small: list = []
        large: list = []
        in_small = [False] * n
        alive = [False] * n
        small_sum = 0
        small_cnt = 0
        large_cnt = 0

        def clean(heap, want_small: bool) -> bool:
            while heap:
                _v, idx = heap[0]
                if not alive[idx] or in_small[idx] != want_small:
                    heapq.heappop(heap)
                else:
                    return True
            return False

        def rebalance():
            nonlocal small_sum, small_cnt, large_cnt
            clean(small, True)
            clean(large, False)
            while small_cnt < need and large_cnt > 0:
                if not clean(large, False):
                    break
                val, idx = heapq.heappop(large)
                large_cnt -= 1
                in_small[idx] = True
                small_sum += val
                small_cnt += 1
                heapq.heappush(small, (-val, idx))
            while small_cnt > need:
                if not clean(small, True):
                    break
                val, idx = heapq.heappop(small)
                val = -val
                small_sum -= val
                small_cnt -= 1
                in_small[idx] = False
                heapq.heappush(large, (val, idx))
                large_cnt += 1
            # The biggest picked value must not beat the smallest unpicked.
            while clean(small, True) and clean(large, False):
                if -small[0][0] > large[0][0]:
                    sv, si = heapq.heappop(small)
                    sv = -sv
                    lv, li = heapq.heappop(large)
                    small_sum += lv - sv
                    in_small[si] = False
                    in_small[li] = True
                    heapq.heappush(small, (-lv, li))
                    heapq.heappush(large, (sv, si))
                else:
                    break

        ans = None
        # Window [L, R] with R = min(L + dist, n - 1); cuts are indices
        # 1..n-1, so the first window starts at L = 1.
        for left in range(1, n):
            right = min(left + dist, n - 1)
            if left == 1:
                for idx in range(1, right + 1):
                    alive[idx] = True
                    heapq.heappush(large, (nums[idx], idx))
                    large_cnt += 1
            else:
                out = left - 1
                if alive[out]:
                    alive[out] = False
                    if in_small[out]:
                        in_small[out] = False
                        small_sum -= nums[out]
                        small_cnt -= 1
                    else:
                        large_cnt -= 1
                if right > left + dist - 1 and right <= n - 1:
                    # The window's right edge moved one step (unless it
                    # already hit n - 1 and stopped moving).
                    prev_right = min(left - 1 + dist, n - 1)
                    if right > prev_right:
                        alive[right] = True
                        heapq.heappush(large, (nums[right], right))
                        large_cnt += 1
            rebalance()
            if small_cnt == need:
                total = nums[0] + small_sum
                if ans is None or total < ans:
                    ans = total
        return ans if ans is not None else nums[0]
