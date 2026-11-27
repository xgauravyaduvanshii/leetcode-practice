# LeetCode 1105. Filling Bookcase Shelves — Medium
# https://leetcode.com/problems/filling-bookcase-shelves/
# Submission 2199000503 — Accepted, Python3
#
# My thinking: I work out the cheapest height
# for every prefix of books. The last shelf can
# hold any run of books that fits the width, and
# its height is the tallest book on it.

from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            width = 0
            height = 0
            dp[i] = float("inf")
            for j in range(i, 0, -1):
                width += books[j - 1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)
        return dp[n]
