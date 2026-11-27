# LeetCode 440. K-th Smallest in Lexicographical Order — Hard
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# Submission 2198658285 — Accepted, Python3
#
# My thinking: from a prefix I count how many numbers
# sit under it — the whole subtree between the prefix
# and the next one. If the k-th number is past that
# subtree I skip to the next sibling, otherwise I
# step down into the subtree.

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def steps_between(first, last):
            steps = 0
            while first <= n:
                steps += min(last, n + 1) - first
                first *= 10
                last *= 10
            return steps

        current = 1
        k -= 1
        while k > 0:
            steps = steps_between(current, current + 1)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1
        return current
