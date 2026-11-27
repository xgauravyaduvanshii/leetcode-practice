# LeetCode 1910. Remove All Occurrences of a Substring — Medium
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
# Submission 2201305864 — Accepted, Python3
#
# My thinking: I walk the string once with a
# stack, and a KMP table tells me how much of
# the part is matched at the end — the moment it
# matches fully, those letters come straight off.

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and part[i] != part[j]:
                j = pi[j - 1]
            if part[i] == part[j]:
                j += 1
            pi[i] = j
        stack = []
        matched = []
        cur = 0
        for ch in s:
            while cur > 0 and ch != part[cur]:
                cur = pi[cur - 1]
            if ch == part[cur]:
                cur += 1
            stack.append(ch)
            matched.append(cur)
            if cur == m:
                del stack[-m:]
                del matched[-m:]
                cur = matched[-1] if matched else 0
        return "".join(stack)
