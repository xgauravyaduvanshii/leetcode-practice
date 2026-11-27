# LeetCode 2179. Count Good Triplets in an Array — Hard
# https://leetcode.com/problems/count-good-triplets-in-an-array/
# Submission 2201602746 — Accepted, Python3
#
# My thinking: a good triplet rises in both
# orders, so I rewrite the first array by
# each value's place in the second — then
# every middle value counts its smaller
# neighbours on the left times its larger
# neighbours on the right, tallied with a
# Fenwick tree.

class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        pos = [0] * n
        for i, v in enumerate(nums2):
            pos[v] = i
        a = [pos[v] for v in nums1]

        def fenwick_add(bit, i, delta):
            i += 1
            while i <= n:
                bit[i] += delta
                i += i & -i

        def fenwick_sum(bit, i):
            # Sum of bit[0..i] (i may be -1, meaning empty).
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        left = [0] * n
        bit = [0] * (n + 1)
        for j in range(n):
            left[j] = fenwick_sum(bit, a[j] - 1)
            fenwick_add(bit, a[j], 1)
        right = [0] * n
        bit = [0] * (n + 1)
        for j in range(n - 1, -1, -1):
            seen = n - 1 - j
            right[j] = seen - fenwick_sum(bit, a[j])
            fenwick_add(bit, a[j], 1)
        return sum(left[j] * right[j] for j in range(n))
