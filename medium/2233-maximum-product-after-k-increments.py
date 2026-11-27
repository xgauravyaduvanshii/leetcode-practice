# LeetCode 2233. Maximum Product After K Increments — Medium
# https://leetcode.com/problems/maximum-product-after-k-increments/
# Submission 2204511892 — Accepted, Python3
#
# My thinking: adding 1 to the smallest element grows the product the
# most, so I use a min-heap and always increment its smallest element,
# k times in total. The final product is taken modulo 10^9 + 7.
class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        for _ in range(k):
            x = heapq.heappop(nums)
            heapq.heappush(nums, x + 1)
        ans = 1
        MOD = 10 ** 9 + 7
        for x in nums:
            ans = ans * x % MOD
        return ans
