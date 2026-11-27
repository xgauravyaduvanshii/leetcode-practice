# LeetCode 1268. Search Suggestions System — Medium
# https://leetcode.com/problems/search-suggestions-system/
# Submission 2199022127 — Accepted, Python3
#
# My thinking: with the products sorted, the
# matches for each typed prefix sit together
# starting at the first product that is not
# smaller than the prefix. I take up to three
# of them.

import bisect
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            start = bisect.bisect_left(products, prefix)
            result.append([p for p in products[start:start + 3] if p.startswith(prefix)])
        return result
