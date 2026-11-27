# LeetCode 3430. Maximum and Minimum Sums of at Most Size K Subarrays — Hard
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/
# Submission 2202526774 — Accepted 684/684, Python3
from typing import List


class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        # My thinking: each element contributes as the max (and
        # separately as the min) of the subarrays it dominates.
        # Monotonic stacks give its reach on both sides; with
        # l left choices and r right choices, l*r pairs exist
        # but those longer than k must go — if l+r-1 exceeds k
        # by `extra`, exactly extra*(extra+1)/2 pairs are too
        # long. I add each element's value times its count.
        def contribution(is_min):
            n = len(nums)
            prev = [-1] * n
            nxt = [n] * n
            st = []
            for i in range(n):
                while st and ((nums[st[-1]] >= nums[i]) if is_min
                             else (nums[st[-1]] <= nums[i])):
                    st.pop()
                prev[i] = st[-1] if st else -1
                st.append(i)
            st = []
            for i in range(n - 1, -1, -1):
                while st and ((nums[st[-1]] > nums[i]) if is_min
                             else (nums[st[-1]] < nums[i])):
                    st.pop()
                nxt[i] = st[-1] if st else n
                st.append(i)
            total = 0
            for i in range(n):
                l = min(i - prev[i], k)
                r = min(nxt[i] - i, k)
                extra = max(0, l + r - 1 - k)
                cnt = l * r - extra * (extra + 1) // 2
                total += nums[i] * cnt
            return total

        return contribution(True) + contribution(False)
