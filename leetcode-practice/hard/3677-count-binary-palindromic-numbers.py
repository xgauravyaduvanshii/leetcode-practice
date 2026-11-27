# LeetCode 3677. Count Binary Palindromic Numbers — Hard
# https://leetcode.com/problems/count-binary-palindromic-numbers/
# Submission 2203034410 — Accepted, Python3
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        # My thinking: a binary palindrome is fixed by its first
        # half — mirror the first half to get the whole number.
        # I count 0 on its own, then every palindrome shorter
        # than n: for a length L the first bit is 1 and the
        # remaining ceil(L/2) - 1 free bits give 2 ** ((L - 1) // 2)
        # palindromes. For n's own length I take the first half
        # of n, count the smaller halves, and add one more only
        # if the palindrome built from n's own half is still <= n.
        if n == 0:
            return 1
        s = bin(n)[2:]
        length = len(s)
        count = 1  # the number 0
        for shorter in range(1, length):
            count += 1 << ((shorter - 1) // 2)
        half_len = (length + 1) // 2
        half = int(s[:half_len], 2)
        base = 1 << (half_len - 1)
        prefix = s[:half_len]
        mirrored = prefix + (prefix[::-1] if length % 2 == 0 else prefix[:-1][::-1])
        count += half - base
        if int(mirrored, 2) <= n:
            count += 1
        return count
