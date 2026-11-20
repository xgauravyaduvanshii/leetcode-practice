# 190. Reverse Bits (Easy)
# https://leetcode.com/problems/reverse-bits/
# Submission 2199956937 — Accepted, Python3
class Solution:
    def reverseBits(self, n: int) -> int:
        # My thinking: walk through the 32 bits of n from
        # the right, and build the answer from the left —
        # every bit we peel off n becomes the next bit of
        # the answer.
        answer = 0
        for _ in range(32):
            answer = (answer << 1) | (n & 1)
            n >>= 1
        return answer
