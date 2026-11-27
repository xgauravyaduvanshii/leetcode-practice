# LeetCode 2384. Largest Palindromic Number — Medium
# https://leetcode.com/problems/largest-palindromic-number/
# Submission 2204774359 — Accepted, Python3
#
# My thinking: count each digit, then build the left half from the
# largest digits down using the available pairs — but never start the
# half with '0' (leading zeros would make the number smaller, and a
# half of only zeros is dropped). The middle is the largest digit with
# an odd count. If nothing is left at all, the answer is '0'.
class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = [0] * 10
        for ch in num:
            cnt[ord(ch) - 48] += 1
        left = []
        for d in range(9, -1, -1):
            pairs = cnt[d] // 2
            if pairs and (d != 0 or left):
                left.append(str(d) * pairs)
        mid = ''
        for d in range(9, -1, -1):
            if cnt[d] % 2 == 1:
                mid = str(d)
                break
        half = ''.join(left)
        ans = half + mid + half[::-1]
        return ans if ans else '0'
