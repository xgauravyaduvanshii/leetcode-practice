# LeetCode 1081. Smallest Subsequence of Distinct Characters — Medium
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# Submission 2198997196 — Accepted, Python3
#
# My thinking: I build the answer left to right.
# A bigger letter already on the stack gets
# dropped when a smaller one arrives — but only
# if that bigger letter appears again later, so
# nothing is lost.

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {ch: i for i, ch in enumerate(s)}
        stack = []
        seen = set()
        for i, ch in enumerate(s):
            if ch in seen:
                continue
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                seen.discard(stack.pop())
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)
