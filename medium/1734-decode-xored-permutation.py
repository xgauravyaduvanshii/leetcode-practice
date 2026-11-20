# LeetCode 1734. Decode XORed Permutation — Medium
# https://leetcode.com/problems/decode-xored-permutation/
# Submission 2199922591 — Accepted, Python3
#
# My thinking: xoring 1 through n gives the
# xor of the whole permutation, and xoring the
# odd-position encodings gives the xor of
# everything but the first number. Those two
# reveal the first number, and the rest follow.

from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total ^= i
        odd_xor = 0
        for i in range(1, len(encoded), 2):
            odd_xor ^= encoded[i]
        first = total ^ odd_xor
        result = [first]
        for value in encoded:
            result.append(result[-1] ^ value)
        return result
