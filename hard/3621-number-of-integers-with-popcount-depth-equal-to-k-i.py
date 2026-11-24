# LeetCode 3621. Number of Integers With Popcount-Depth Equal to K I — Hard
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/
# Submission 2202884591 — Accepted, Python3
import math


class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        # My thinking: the depth of x is one plus the depth of its
        # popcount, so the depth of any number is decided by a
        # popcount of at most 50. I work out the depth of every
        # value up to 50 once, collect the popcounts whose depth is
        # k-1, and count the numbers up to n with one of those
        # popcounts by walking the bits of n. The number 1 itself
        # has popcount 1 but depth 0, so when k is 1 I take it back
        # out of the count.
        def depth(x):
            d = 0
            while x != 1:
                x = bin(x).count("1")
                d += 1
            return d

        dep = {m: depth(m) for m in range(1, 51)}
        if k == 0:
            return 1
        P = [m for m in range(1, 51) if dep[m] == k - 1]
        if not P:
            return 0

        def count_leq(N, c):
            bits = bin(N)[2:]
            L = len(bits)
            count = 0
            ones = 0
            for i, ch in enumerate(bits):
                if ch == '1':
                    rem = L - i - 1
                    need = c - ones
                    if 0 <= need <= rem:
                        count += math.comb(rem, need)
                    ones += 1
                    if ones > c:
                        return count
            if ones == c:
                count += 1
            return count

        total = sum(count_leq(n, c) for c in P)
        if k == 1:
            total -= 1
        return total
