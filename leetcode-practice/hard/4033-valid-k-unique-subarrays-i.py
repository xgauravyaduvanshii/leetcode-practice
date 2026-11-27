# LeetCode 4033. Valid K-Unique Subarrays I — Hard
# https://leetcode.com/problems/valid-k-unique-subarrays-i/
# Submission 2203524018 — Accepted, Python3
from typing import List


def _splitmix64(x: int) -> int:
    # My thinking: splitmix64 gives each distinct value
    # a well-spread 64-bit hash; two calls with different
    # salts give two independent hashes.
    x = (x + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
    return x ^ (x >> 31)


class Solution:
    def validSubarrays(self, nums: List[int], k: int, queries: List[List[int]]) -> List[bool]:
        # My thinking: a subarray is valid exactly when
        # it has k distinct numbers and every number in
        # it occurs an even number of times. Both checks
        # are answered with prefix structures. For parity,
        # give every value two independent 64-bit hashes
        # (splitmix64 with different salts) and keep
        # their prefix XORs: a value occurring an even
        # number of times cancels itself out, so the XOR
        # over a range is zero exactly when every value
        # in the range occurs an even number of times.
        # One 64-bit hash is not enough — a single random
        # XOR hash collided on a test with 135
        # odd-frequency values and gave a false positive —
        # so two independent hashes are used and both
        # must be zero. For the distinct count, answer
        # the queries offline sorted by right end with a
        # Fenwick tree over last occurrences: scanning
        # right, each position contributes +1 and its
        # previous occurrence -1, so a range sum is the
        # number of distinct values in that range.
        n = len(nums)
        maxv = max(nums)
        hv1 = [0] * (maxv + 1)
        hv2 = [0] * (maxv + 1)
        for v in range(1, maxv + 1):
            hv1[v] = _splitmix64(v ^ 0x9E3779B97F4A7C15)
            hv2[v] = _splitmix64(v ^ 0xC2B2AE3D27D4EB4F)
        p1 = [0] * (n + 1)
        p2 = [0] * (n + 1)
        for i, v in enumerate(nums):
            p1[i + 1] = p1[i] ^ hv1[v]
            p2[i + 1] = p2[i] ^ hv2[v]

        q = len(queries)
        order = sorted(range(q), key=lambda i: queries[i][1])
        bit = [0] * (n + 2)

        def bit_add(i: int, d: int) -> None:
            i += 1
            while i <= n + 1:
                bit[i] += d
                i += i & -i

        def bit_sum(i: int) -> int:
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        last = {}
        distinct = [0] * q
        cur = 0
        for qi in order:
            l, r = queries[qi]
            while cur <= r:
                v = nums[cur]
                if v in last:
                    bit_add(last[v], -1)
                bit_add(cur, 1)
                last[v] = cur
                cur += 1
            distinct[qi] = bit_sum(r) - (bit_sum(l - 1) if l > 0 else 0)

        ans = []
        for i, (l, r) in enumerate(queries):
            ok = distinct[i] == k and (p1[r + 1] ^ p1[l]) == 0 and (p2[r + 1] ^ p2[l]) == 0
            ans.append(ok)
        return ans
