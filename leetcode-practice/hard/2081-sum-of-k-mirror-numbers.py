# LeetCode 2081. Sum of k-Mirror Numbers — Hard
# https://leetcode.com/problems/sum-of-k-mirror-numbers/
# Submission 2201567356 — Accepted, Python3
#
# My thinking: a k-mirror number reads the same
# in base ten and in base k, so I build the
# base-ten palindromes in order from their first
# half and keep the ones that also mirror in
# base k, until I have enough.

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_pal_base_k(x):
            digits = []
            while x > 0:
                digits.append(x % k)
                x //= k
            return digits == digits[::-1]

        total = 0
        found = 0
        length = 1
        while found < n:
            half_len = (length + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            for half in range(start, end):
                s = str(half)
                if length % 2 == 0:
                    pal = int(s + s[::-1])
                else:
                    pal = int(s + s[-2::-1])
                if is_pal_base_k(pal):
                    total += pal
                    found += 1
                    if found == n:
                        return total
            length += 1
        return total
