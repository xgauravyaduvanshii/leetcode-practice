# LeetCode 2607. Make K-Subarray Sums Equal — Medium
# https://leetcode.com/problems/make-k-subarray-sums-equal/
# Submission 2205100362 — Accepted, Python3
#
# My thinking: the array is circular, so the positions forced
# equal are the residue classes modulo gcd(n, k) — not modulo
# k. Within each class, the cheapest common value is the
# median, and the cost is the sum of absolute deviations.
import math


class Solution:
    def makeSubKSumEqual(self, arr: list[int], k: int) -> int:
        n = len(arr)
        g = math.gcd(n, k)
        ans = 0
        for r in range(g):
            group = sorted(arr[i] for i in range(r, n, g))
            med = group[len(group) // 2]
            ans += sum(abs(x - med) for x in group)
        return ans
