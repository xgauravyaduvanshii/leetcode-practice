# LeetCode 2269. Find the K-Beauty of a Number — Easy
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/
# Submission 2197620875 — Accepted, Python3
#
# My thinking: I look at every substring of length k
# in the number's digits. A substring counts when it
# is not zero and divides the whole number evenly.

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0
        for i in range(len(s) - k + 1):
            d = int(s[i:i + k])
            if d != 0 and num % d == 0:
                count += 1
        return count
