# LeetCode 779. K-th Symbol in Grammar — Medium
# https://leetcode.com/problems/k-th-symbol-in-grammar/
# Submission 2198933286 — Accepted, Python3
#
# My thinking: each row is built from the one
# above it, so the symbol at position k comes from
# its parent. An odd position copies the parent,
# an even one flips it — I follow the parents up
# to the first row.

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        if k % 2 == 1:
            return parent
        return 1 - parent
