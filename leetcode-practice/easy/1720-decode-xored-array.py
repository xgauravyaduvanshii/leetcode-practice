# LeetCode 1720. Decode XORed Array — Easy
# https://leetcode.com/problems/decode-xored-array/
# Submission 2197595326 — Accepted, Python3
#
# My thinking: each encoded value is the xor of two
# neighbours in the original array. Since I know
# the first number, I can rebuild the rest one by
# one — the next number is the last one I found
# xored with the next encoded value.

class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        ans = [first]
        for x in encoded:
            ans.append(ans[-1] ^ x)
        return ans
