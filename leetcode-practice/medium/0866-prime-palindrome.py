# LeetCode 866. Prime Palindrome — Medium
# https://leetcode.com/problems/prime-palindrome/
# Submission 2198957808 — Accepted, Python3
#
# My thinking: I build palindromes directly by
# mirroring the first half of the digits, shortest
# first. Even-length palindromes are always
# divisible by 11, so only odd lengths can be
# prime — except 11 itself.

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            if num % 2 == 0:
                return num == 2
            d = 3
            while d * d <= num:
                if num % d == 0:
                    return False
                d += 2
            return True

        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11
        length = len(str(n))
        while True:
            if length % 2 == 0:
                length += 1
                continue
            half_len = (length + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            for half in range(start, end):
                text = str(half)
                candidate = int(text + text[-2::-1])
                if candidate >= n and is_prime(candidate):
                    return candidate
            length += 1
