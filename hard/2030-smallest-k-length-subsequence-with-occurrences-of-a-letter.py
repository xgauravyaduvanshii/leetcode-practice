# LeetCode 2030. Smallest K-Length Subsequence With Occurrences of a Letter — Hard
# https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/
# Submission 2201554041 — Accepted, Python3
#
# My thinking: I build the smallest answer with
# a stack, always dropping a bigger letter when
# a smaller one arrives — but only if enough
# letters and enough room are still left to
# finish the length and the count.

class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        remain = s.count(letter)
        stack = []
        have = 0
        for i, ch in enumerate(s):
            while stack and stack[-1] > ch:
                if len(stack) - 1 + (n - i) < k:
                    break
                if stack[-1] == letter and have - 1 + remain < repetition:
                    break
                if stack[-1] == letter:
                    have -= 1
                stack.pop()
            if len(stack) < k:
                if ch == letter:
                    stack.append(ch)
                    have += 1
                else:
                    need = repetition - have
                    if need <= remain and need <= k - len(stack) - 1:
                        stack.append(ch)
            if ch == letter:
                remain -= 1
        return "".join(stack)
