# LeetCode 2183. Count Array Pairs Divisible by K — Hard
# https://leetcode.com/problems/count-array-pairs-divisible-by-k/
# Submission 2201604706 — Accepted, Python3
#
# My thinking: whether two numbers multiply
# to a multiple of k depends only on what
# each shares with k, so I count how many
# numbers share each divisor and pair the
# divisors whose product k divides.

import math
from collections import Counter


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        freq = Counter(math.gcd(x, k) for x in nums)
        divs = sorted(freq)
        ans = 0
        for i, d1 in enumerate(divs):
            for d2 in divs[i:]:
                if (d1 * d2) % k == 0:
                    if d1 == d2:
                        ans += freq[d1] * (freq[d1] - 1) // 2
                    else:
                        ans += freq[d1] * freq[d2]
        return ans
