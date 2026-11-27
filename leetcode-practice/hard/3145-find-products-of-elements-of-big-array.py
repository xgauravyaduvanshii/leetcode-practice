# LeetCode 3145. Find Products of Elements of Big Array — Hard
# https://leetcode.com/problems/find-products-of-elements-of-big-array/
# Submission 2202035859 — Accepted, Python3
#
# My thinking: the big array lists the
# powers of two in each integer's binary
# expansion, so the product over a range
# is 2 raised to the sum of the
# exponents. I compute, for any prefix,
# that total exponent sum by walking the
# binary blocks of the prefix — each
# block of size 2^b contributes a known
# count — and answer each query from two
# prefix sums with modular exponentiation.

from typing import List


class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def prefix_exp_sum(p: int) -> int:
            if p < 0:
                return 0
            rem = p
            prefix = 0
            pp = 0
            pe = 0
            exp_sum = 0
            for b in range(60, -1, -1):
                size = 1 << b
                if b == 0:
                    block_pop = pp
                    block_exp = pe
                else:
                    block_pop = size * pp + b * (size // 2)
                    block_exp = size * pe + (size // 2) * b * (b - 1) // 2
                if rem >= block_pop:
                    rem -= block_pop
                    exp_sum += block_exp
                    prefix |= size
                    pp += 1
                    pe += b
            need = rem + 1
            partial = 0
            bit = 0
            while need > 0:
                if (prefix >> bit) & 1:
                    partial += bit
                    need -= 1
                bit += 1
            return exp_sum + partial

        cache = {}

        def cached(p: int) -> int:
            if p not in cache:
                cache[p] = prefix_exp_sum(p)
            return cache[p]

        ans = []
        for frm, to, mod in queries:
            if mod == 1:
                ans.append(0)
                continue
            exp = cached(to) - cached(frm - 1)
            ans.append(pow(2, exp, mod))
        return ans
