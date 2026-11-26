# LeetCode 3855. Sum of K-Digit Numbers in a Range — Hard
# https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/
# Submission 2203296689 — Accepted, Python3


class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        # My thinking: every position of the k-digit number
        # contributes independently. A digit d appears in one
        # fixed position in exactly m^(k-1) of the numbers,
        # where m = r - l + 1 is how many digits are allowed,
        # so a single position contributes (l + ... + r) *
        # m^(k-1), and the positions are weighted 1, 10, ...,
        # 10^(k-1), a geometric series summing to (10^k - 1)
        # / 9. The whole sum is therefore S * m^(k-1) *
        # (10^k - 1) / 9 modulo 1e9 + 7, with the division
        # done by the modular inverse of 9 and the powers by
        # fast exponentiation, which also handles k up to 1e9.
        mod = 10 ** 9 + 7
        m = r - l + 1
        digit_sum = (l + r) * m // 2
        geo = (pow(10, k, mod) - 1) * pow(9, mod - 2, mod) % mod
        return digit_sum % mod * pow(m, k - 1, mod) % mod * geo % mod
