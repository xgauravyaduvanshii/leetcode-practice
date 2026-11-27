# LeetCode 1497. Check If Array Pairs Are Divisible by k — Medium
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
# Submission 2199864316 — Accepted, Python3
#
# My thinking: two numbers pair up when their
# remainders add to k. So every remainder's
# count must match its complement's — and
# remainders that pair with themselves need an
# even count.

from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts = Counter(x % k for x in arr)
        for r, count in counts.items():
            if r == 0 or 2 * r == k:
                if count % 2:
                    return False
            elif counts[r] != counts[k - r]:
                return False
        return True
