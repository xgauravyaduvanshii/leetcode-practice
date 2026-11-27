# LeetCode 3962. Maximum Subarray Sum After at Most K Swaps — Hard
# https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/
# Submission 2203484697 — Accepted, Python3
import heapq
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # My thinking: a swap can only change a window by
        # taking one element out of it and bringing one
        # element in from outside, so for a fixed window the
        # best use of t swaps is to drop its t smallest
        # elements and bring in the t largest elements from
        # outside the window. The gain of the j-th such swap
        # falls as j grows, so the best t is where the gains
        # stop being positive. I keep that t with four heaps
        # while the window grows: the smallest inside
        # elements, the rest of the inside, the largest
        # outside elements, and the rest of the outside.
        # Each new right end moves one element from outside
        # to inside, and each new left end rebuilds the
        # heaps. Adjusting t is cheap in the long run: a new
        # element can only raise the best t by one, and t
        # can only fall as far as it rose.
        n = len(nums)
        ans = -10 ** 18
        for l in range(n):
            # in_small: max-heap (-v, i) of the t smallest
            #   inside elements; in_rest: min-heap (v, i)
            #   of the other inside elements; out_big:
            #   min-heap (v, i) of the t largest outside
            #   elements; out_rest: max-heap (-v, i) of the
            #   other outside elements.
            in_small = []
            in_rest = [(nums[l], l)]
            out_big = []
            out_rest = [(-nums[i], i) for i in range(n) if i != l]
            heapq.heapify(out_rest)
            removed = [False] * n
            loc = [3] * n
            loc[l] = 1
            window_sum = nums[l]
            swaps = 0
            sum_small = 0
            sum_big = 0

            def clean(heap):
                while heap and removed[heap[0][1]]:
                    heapq.heappop(heap)

            def adjust(right):
                nonlocal swaps, sum_small, sum_big
                cap = k if k < right - l + 1 else right - l + 1
                while swaps < cap:
                    clean(out_rest)
                    if not out_rest or not in_rest:
                        break
                    if -out_rest[0][0] > in_rest[0][0]:
                        v, u = heapq.heappop(out_rest)
                        heapq.heappush(out_big, (-v, u))
                        loc[u] = 2
                        sum_big += -v
                        v2, u2 = heapq.heappop(in_rest)
                        heapq.heappush(in_small, (-v2, u2))
                        loc[u2] = 0
                        sum_small += v2
                        swaps += 1
                    else:
                        break
                while swaps > 0:
                    clean(out_big)
                    if not out_big:
                        break
                    if out_big[0][0] < -in_small[0][0]:
                        v, u = heapq.heappop(out_big)
                        heapq.heappush(out_rest, (-v, u))
                        loc[u] = 3
                        sum_big -= v
                        negv, u2 = heapq.heappop(in_small)
                        heapq.heappush(in_rest, (-negv, u2))
                        loc[u2] = 1
                        sum_small += negv
                        swaps -= 1
                    else:
                        break

            adjust(l)
            ans = max(ans, window_sum - sum_small + sum_big)
            for r in range(l + 1, n):
                x = nums[r]
                if loc[r] == 2:
                    removed[r] = True
                    sum_big -= x
                    clean(out_rest)
                    if out_rest:
                        v, u = heapq.heappop(out_rest)
                        heapq.heappush(out_big, (-v, u))
                        loc[u] = 2
                        sum_big += -v
                    else:
                        negv, u2 = heapq.heappop(in_small)
                        heapq.heappush(in_rest, (-negv, u2))
                        loc[u2] = 1
                        sum_small += negv
                        swaps -= 1
                else:
                    removed[r] = True
                if swaps > 0:
                    heapq.heappush(in_small, (-x, r))
                    sum_small += x
                    negv, u = heapq.heappop(in_small)
                    sum_small += negv
                    heapq.heappush(in_rest, (-negv, u))
                    loc[u] = 1
                    loc[r] = 0 if u != r else 1
                else:
                    heapq.heappush(in_rest, (x, r))
                    loc[r] = 1
                window_sum += x
                adjust(r)
                ans = max(ans, window_sum - sum_small + sum_big)
        return ans
