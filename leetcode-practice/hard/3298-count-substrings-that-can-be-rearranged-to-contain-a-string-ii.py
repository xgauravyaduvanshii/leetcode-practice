# LeetCode 3298. Count Substrings That Can Be Rearranged to Contain a String II — Hard
# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/
# Submission 2202185775 — Accepted, Python3
#
# My thinking: a substring works when it holds
# at least as many of each letter as word2 needs.
# I slide a window with two pointers, tracking
# how many distinct needed letters are satisfied;
# once the window is valid, every extension to
# the right is valid too, so I add them all and
# then shrink from the left.

from typing import List


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        need = [0] * 26
        for ch in word2:
            need[ord(ch) - 97] += 1
        distinct = sum(1 for x in need if x)
        cnt = [0] * 26
        a = [ord(ch) - 97 for ch in word1]
        n = len(a)
        satisfied = 0
        right = 0
        ans = 0
        for left in range(n):
            while right < n and satisfied < distinct:
                c = a[right]
                cnt[c] += 1
                if cnt[c] == need[c]:
                    satisfied += 1
                right += 1
            if satisfied < distinct:
                break
            ans += n - right + 1
            c = a[left]
            if cnt[c] == need[c]:
                satisfied -= 1
            cnt[c] -= 1
        return ans
